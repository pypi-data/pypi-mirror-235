import os, re, logging
from dotenv import load_dotenv
from datetime import datetime, timedelta

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from sqlalchemy import and_
from sqlalchemy.orm import Session

import sys
sys.path.append('.')

import sigan.src.utils as global_utils
import sigan.src.application.utils as utils
import sigan.src.application.exceptions as exceptions
import sigan.src.application.blocks as blocks
import sigan.src.persistence.models as models
import sigan.src.persistence.repositories as router
from sigan.src.config import configs



load_dotenv('.env')

# client = WebClient(token=os.environ.get('SLACK_BOT_TOKEN'))
logger = logging.getLogger(__name__)


def create_alarm(db: Session, alarm: dict):
    post_time = datetime.strptime(alarm['alarm_date'], '%Y-%m-%d %H:%M:%S')
    
    if alarm['interval']:
        alarm['alarm_date'] = alarm['alarm_date'].split(" ")[1][:5]
    
    if alarm['slack_channel_name'] == "SiganBot":
        channel_id = get_bot_channel(db, alarm['slack_channel_name'])
    else:
        channel_id = get_channel_id(db, alarm['slack_channel_name'])
        
    if channel_id is None:
        raise exceptions.SlackChannelNotFound()
    
    client = get_client(db)
    
    try:
        response = client.chat_scheduleMessage(
            channel = channel_id,
            text = alarm['content'],
            blocks = blocks.alarm_blocks(alarm),
            post_at = int(post_time.timestamp()),
        )
    except SlackApiError as e:
        return {"success": False, "error": e.response['error']}
    
    alarm['scheduled_message_id'] = response['scheduled_message_id']
    alarm['slack_channel_id'] = channel_id
    alarm['user_id'] = get_user_id(db)
    
    if alarm['confirm_alarm_date']:
        alarm['sub_scheduled_message_id'] = create_confirm_alarm(db, alarm)
    
    router.create_alarm(db, alarm)
    
    return {"success": True, "new_alarm": alarm}


def delete_alarm(db: Session, alarm_id: int):
    alarm_id_cache = global_utils.read_alarm_id(configs.APP_DIR)
    if alarm_id > len(alarm_id_cache) or alarm_id == 0:
        raise exceptions.AlarmNotFoundException(alarm_id=alarm_id)
    delete_alarm_id = alarm_id_cache[str(alarm_id)]
    
    alarm = db.query(models.Alarm).filter(models.Alarm.alarm_id==delete_alarm_id).first()    
    alarm_dict = global_utils.sql_obj_to_dict(alarm)
    
    if alarm_dict['deadline']:
        year, month, day = utils.change_deadline_to_date(alarm_dict['deadline'])
        time = alarm_dict['alarm_date']
        if re.match("^([0-9]){4}-([0-9]){1,2}-([0-9]){1,2}|([0-9]){1,2}-([0-9]){1,2} [0-9]{2}:[0-9]{2}:[0-9]{2}$", time):
            time = alarm_dict['alarm_date'].split(" ")[1][:5]

        deadline = datetime.strptime(f"{year}-{month}-{day} {time}:00", '%Y-%m-%d %H:%M:%S')
        if deadline < datetime.now():
            router.delete_alarm(db, alarm)
            return {"success": True}
    
    post_at = list_scheduled_messages(db, alarm_dict['slack_channel_id'], alarm_dict['scheduled_message_id'])
    if post_at is None:
        if alarm_dict['confirm_alarm_date']:
            delete_confirm_alarm(db, alarm_id)
        router.delete_alarm(db, alarm)
        return {"success": True}
    
    alarm_date = datetime.fromtimestamp(post_at)
    if alarm_date - timedelta(minutes=5) < datetime.now():
        raise exceptions.AlarmConditionalFalse()
    
    client = get_client(db)
    
    try:
        client.chat_deleteScheduledMessage(
            channel=alarm_dict['slack_channel_id'],
            scheduled_message_id=alarm_dict['scheduled_message_id']
        )
    except SlackApiError as e:
        return {"success": False, "error": e.response['error']}
    
    if alarm_dict['deadline']:
        delete_confirm_alarm(db, alarm_id)
    
    router.delete_alarm(db, alarm)
    
    return {"success": True}


def change_content(db: Session, change_alarm: dict):
    alarm_id_cache = global_utils.read_alarm_id(configs.APP_DIR)
    if change_alarm['alarm_id'] > len(alarm_id_cache) or change_alarm['alarm_id'] == 0:
        raise exceptions.AlarmNotFoundException(alarm_id=change_alarm['alarm_id'])
    change_alarm_id = alarm_id_cache[str(change_alarm['alarm_id'])]
    
    alarm = db.query(models.Alarm).filter(models.Alarm.alarm_id==change_alarm_id).first()   
    alarm_dict = global_utils.sql_obj_to_dict(alarm)
    
    if re.match("^[0-9]{2}:[0-9]{2}$", alarm_dict['alarm_date']):
        interval_list = alarm_dict['interval'].split(" ")
        if interval_list[0] == "every":
            interval_list = interval_list[1:]
        
        year, month, day = utils.get_date_from_shortcut(interval_list, alarm_dict['alarm_date'])
        alarm_dict['alarm_date'] = f"{year}-{month}-{day} {alarm_dict['alarm_date']}:00"
    
    alarm_dict['content'] = change_alarm['content']

    try:
        deleted_alarm = delete_alarm(db, change_alarm['alarm_id'])
        if deleted_alarm['success'] is False:
            return {"success": False, "error": deleted_alarm['error']}
        
        new_alarm = create_alarm(db, alarm_dict)
        if new_alarm['success'] is False:
            return {"success": False, "error": new_alarm['error']}
    except Exception as e:
        return {"success": False, "error": e.error}
    
    router.change_content(db, new_alarm['new_alarm'], alarm)

    return {"success": True}


def change_deadline(db: Session, change_alarm: dict):
    alarm_id_cache = global_utils.read_alarm_id(configs.APP_DIR)
    if change_alarm['alarm_id'] > len(alarm_id_cache) or change_alarm['alarm_id'] == 0:
        raise exceptions.AlarmNotFoundException(alarm_id=change_alarm['alarm_id'])
    change_alarm_id = alarm_id_cache[str(change_alarm['alarm_id'])]
    
    alarm = db.query(models.Alarm).filter(models.Alarm.alarm_id==change_alarm_id).first()
    alarm_dict = global_utils.sql_obj_to_dict(alarm)
    
    if alarm_dict['deadline'] is None:
        raise exceptions.DeadlineNotSet()
    
    cur_deadline_year, cur_deadline_month, cur_deadline_day = utils.change_deadline_to_date(alarm_dict['deadline'])
    new_deadline_year, new_deadline_month, new_deadline_day = utils.change_deadline_to_date(change_alarm['deadline'])
    
    if re.match("^([0-9]){4}-([0-9]){1,2}-([0-9]){1,2}|([0-9]){1,2}-([0-9]){1,2} [0-9]{2}:[0-9]{2}:[0-9]{2}$", alarm_dict['alarm_date']):
        alarm_time = alarm_dict['alarm_date'].split(" ")[1][:5]
        cur_deadline_date = datetime.strptime(f"{cur_deadline_year}-{cur_deadline_month}-{cur_deadline_day} {alarm_time}:00", '%Y-%m-%d %H:%M:%S')
        new_deadline_date = datetime.strptime(f"{new_deadline_year}-{new_deadline_month}-{new_deadline_day} {alarm_time}:00", '%Y-%m-%d %H:%M:%S')
        cur_alarm_date = datetime.strptime(alarm_dict['alarm_date'], '%Y-%m-%d %H:%M:%S')

    elif re.match("^[0-9]{2}:[0-9]{2}$", alarm_dict['alarm_date']):
        interval_list = alarm_dict['interval'].split(" ")
        if interval_list[0] == "every":
            interval_list = interval_list[1:]
        
        year, month, day = utils.get_date_from_shortcut(interval_list, alarm_dict['alarm_date'])
        alarm_date = f"{year}-{month}-{day} {alarm_dict['alarm_date']}:00"
        
        cur_deadline_date = datetime.strptime(f"{cur_deadline_year}-{cur_deadline_month}-{cur_deadline_day} {alarm_dict['alarm_date']}:00", '%Y-%m-%d %H:%M:%S')
        new_deadline_date = datetime.strptime(f"{new_deadline_year}-{new_deadline_month}-{new_deadline_day} {alarm_dict['alarm_date']}:00", '%Y-%m-%d %H:%M:%S')
        cur_alarm_date = datetime.strptime(alarm_date, '%Y-%m-%d %H:%M:%S')
        
        alarm_dict['alarm_date'] = alarm_date
    
    if new_deadline_date < cur_alarm_date:
        raise exceptions.DeadlineEarlierThanAlarmSet()
    
    confirm_alarm_day = alarm_dict['confirm_alarm_date'] - cur_deadline_date
    alarm_dict['confirm_alarm_date'] = new_deadline_date + confirm_alarm_day
    alarm_dict['deadline'] = change_alarm['deadline']
    
    try:
        deleted_alarm = delete_alarm(db, change_alarm['alarm_id'])
        if deleted_alarm['success'] is False:
            return {"success": False, "error": deleted_alarm['error']} 
        
        new_alarm = create_alarm(db, alarm_dict)
        if new_alarm['success'] is False:
            return {"success": False, "error": new_alarm['error']}       
    except Exception as e:
        return {"success": False, "error": e.error}
    
    router.change_deadline(db, new_alarm['new_alarm'], alarm)

    return {"success": True}


def change_date(db: Session, change_alarm: dict):
    alarm_id_cache = global_utils.read_alarm_id(configs.APP_DIR)
    change_alarm_id = alarm_id_cache[str(change_alarm['alarm_id'])]
    
    alarm = db.query(models.Alarm).filter(models.Alarm.alarm_id==change_alarm_id).first()    
    alarm_dict = global_utils.sql_obj_to_dict(alarm)
    
    if alarm_dict['interval']:
        if not re.match("^[0-9]{2}:[0-9]{2}$", change_alarm['alarm_date']):
            raise exceptions.InvalidDateSetting()
        
        interval_list = alarm_dict['interval'].split(" ")
        if interval_list[0] == "every":
            interval_list = interval_list[1:]
            
        year, month, day = utils.get_date_from_shortcut(interval_list, change_alarm['alarm_date'])
        alarm_date = f"{year}-{month}-{day} {change_alarm['alarm_date']}:00"
    else:
        # 시간만 변경하고자 하는 경우
        if re.match("^[0-9]{2}:[0-9]{2}$", change_alarm['alarm_date']):
            current_date = alarm_dict['alarm_date'].split(" ")[0]
            alarm_date = f"{current_date} {change_alarm['alarm_date']}:00"
        # 날짜만 변경하고자 하는 경우
        elif re.match("^([0-9]){4}-([0-9]){1,2}-([0-9]){1,2}$", change_alarm['alarm_date']):
            alarm_time = alarm_dict['alarm_date'].split(" ")[1]
            alarm_date = f"{change_alarm['alarm_date']} {alarm_time}"
        # 날짜와 시간 모두 변경하고자 하는 경우
        elif re.match("^([0-9]){4}-([0-9]){1,2}-([0-9]){1,2} [0-9]{2}:[0-9]{2}:[0-9]{2}$", change_alarm['alarm_date']):
            alarm_date = change_alarm['alarm_date']
    
    alarm_dict['alarm_date'] = alarm_date
    
    try:
        deleted_alarm = delete_alarm(db, change_alarm['alarm_id'])
        if deleted_alarm['success'] is False:
            return {"success": False, "error": deleted_alarm['error']} 
        
        new_alarm = create_alarm(db, alarm_dict)
        if new_alarm['success'] is False:
            return {"success": False, "error": new_alarm['error']}       
    except Exception as e:
        return {"success": False, "error": e.error}
    
    router.change_date(db, new_alarm['new_alarm'], alarm)

    return {"success": True}


def change_interval(db: Session, change_alarm: dict):
    alarm_id_cache = global_utils.read_alarm_id(configs.APP_DIR)
    change_alarm_id = alarm_id_cache[str(change_alarm['alarm_id'])]
    
    alarm = db.query(models.Alarm).filter(models.Alarm.alarm_id==change_alarm_id).first()    
    alarm_dict = global_utils.sql_obj_to_dict(alarm)
    
    if re.match("^([0-9]){4}-([0-9]){1,2}-([0-9]){1,2} [0-9]{2}:[0-9]{2}:[0-9]{2}$", alarm_dict['alarm_date']):
        raise exceptions.InvalidIntervalSetting()
    
    interval_list = change_alarm['interval'].split(" ")
    if interval_list[0] == "every":
        interval_list = interval_list[1:]
    
    year, month, day = utils.get_date_from_shortcut(interval_list, alarm_dict['alarm_date'])
    alarm_date = f"{year}-{month}-{day} {alarm_dict['alarm_date']}:00"
    
    alarm_dict['alarm_date'] = alarm_date
    alarm_dict['interval'] = change_alarm['interval']
    
    try:
        deleted_alarm = delete_alarm(db, change_alarm['alarm_id'])
        if deleted_alarm['success'] is False:
            return {"success": False, "error": deleted_alarm['error']} 
        
        new_alarm = create_alarm(db, alarm_dict)
        if new_alarm['success'] is False:
            return {"success": False, "error": new_alarm['error']}       
    except Exception as e:
        return {"success": False, "error": e.error}
    
    router.change_interval(db, new_alarm['new_alarm'], alarm)

    return {"success": True, "alarm_obj": alarm, "new_alarm_dict": new_alarm['new_alarm']}


def list_scheduled_messages(db: Session, channel_id: str, scheduled_message_id: str):
    client = get_client(db)
    response = client.chat_scheduledMessages_list(channel=channel_id)
    if response is None:
        return None
    
    for message in response['scheduled_messages']:
        if message['id'] == scheduled_message_id:
            return message['post_at']


def get_channel_id(db: Session, channel_name: str):
    client = get_client(db)
    channels = client.conversations_list(types="public_channel,private_channel")["channels"]
    for channel in channels:
        if channel["name"] == channel_name:
            return channel["id"]
    
    return None


def get_bot_channel(db: Session, channel_name: str):
    channel = db.query(models.User).filter(models.User.channel_name==channel_name).first()
    return channel.channel_id


def get_all_alarms(db: Session, user_id: int):
    alarm = db.query(models.Alarm).filter(models.Alarm.user_id==user_id).all()
    alarm_dict_list = global_utils.sql_obj_list_to_dict_list(alarm)
    
    alarm_id_cache = {}
    for i in range(len(alarm_dict_list)):
        alarm_id_cache[i + 1] = alarm_dict_list[i]['alarm_id']
         
    global_utils.cache_alarm_id(configs.APP_DIR, alarm_id_cache)
    
    return alarm_dict_list
    

def create_confirm_alarm(db: Session, alarm: dict):
    post_time = alarm['confirm_alarm_date']
    
    if alarm['slack_channel_name'] == "SiganBot":
        channel_id = get_bot_channel(db, alarm['slack_channel_name'])
    else:
        channel_id = get_channel_id(db, alarm['slack_channel_name'])
    
    client = get_client(db)
    
    response = client.chat_scheduleMessage(
        channel = channel_id,
        text = alarm['content'],
        blocks = blocks.alarm_blocks(alarm),
        post_at = int(post_time.timestamp()),
    )
    return response['scheduled_message_id']


def delete_confirm_alarm(db: Session, alarm_id: int):
    alarm_id_cache = global_utils.read_alarm_id(configs.APP_DIR)
    delete_alarm_id = alarm_id_cache[str(alarm_id)]
    
    alarm = db.query(models.Alarm).filter(models.Alarm.alarm_id==delete_alarm_id).first()
    if not alarm:
        raise exceptions.AlarmNotFoundException(alarm_id=delete_alarm_id)
    
    client = get_client(db)

    client.chat_deleteScheduledMessage(
        channel=alarm.slack_channel_id,
        scheduled_message_id=alarm.sub_scheduled_message_id
    )


def get_client(db: Session):
    slack_info = global_utils.read_team_id(configs.APP_DIR)
    user_info = db.query(models.User).filter(models.User.team_id==slack_info['team_id']).first()
    client = WebClient(token=user_info.access_token)
    return client


def get_user_id(db: Session):
    slack_info = global_utils.read_team_id(configs.APP_DIR)
    if slack_info is None:
        return None
    
    user_info = db.query(models.User).filter(models.User.team_id==slack_info['team_id']).first()
    return user_info.user_id


def match_team_id(db: Session, team_id: str):
    user = db.query(models.User).filter(models.User.team_id==team_id).first()
    if user is None:
        return None
    return user.team_id