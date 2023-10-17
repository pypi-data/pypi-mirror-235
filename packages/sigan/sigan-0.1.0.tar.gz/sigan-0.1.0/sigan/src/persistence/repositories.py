import os
from dotenv import load_dotenv
from slack_sdk import WebClient
from sqlalchemy.orm import Session

import sys
sys.path.append('.')

import sigan.src.persistence.models as models


load_dotenv('.env')


def create_alarm(db: Session, alarm: dict):
    new_alarm = models.Alarm(**alarm)
    
    db.add(new_alarm)
    db.commit()
    db.refresh(new_alarm)
    
    return {"success": True, "new_alarm": new_alarm}


def delete_alarm(db: Session, alarm_obj):

    db.delete(alarm_obj)
    db.commit()
    
    return {"success": True}


def change_content(db: Session, change_alarm: dict, alarm_obj):
    
    setattr(alarm_obj, 'content', change_alarm['content'])
    setattr(alarm_obj, 'scheduled_message_id', change_alarm['scheduled_message_id'])
    db.commit()
    
    return {"success": True}


def change_deadline(db: Session, change_alarm: dict, alarm_obj):
    
    setattr(alarm_obj, 'deadline', change_alarm['deadline'])
    setattr(alarm_obj, 'scheduled_message_id', change_alarm['scheduled_message_id'])
    db.commit()
    
    return {"success": True}


def change_date(db: Session, change_alarm: dict, alarm_obj):
    
    setattr(alarm_obj, 'alarm_date',change_alarm['alarm_date'])
    setattr(alarm_obj, 'scheduled_message_id',change_alarm['scheduled_message_id'])
    db.commit()
    
    return {"success": True}


def change_interval(db: Session, change_alarm: dict, alarm_obj):
    
    setattr(alarm_obj, 'interval', change_alarm['interval'])
    setattr(alarm_obj, 'scheduled_message_id', change_alarm['scheduled_message_id'])
    db.commit()
    
    return {"success": True}