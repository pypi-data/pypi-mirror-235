class AlarmNotFoundException(Exception):
    def __init__(self, alarm_id):
        self.error = f"Alarm id {alarm_id} is not found."
        
        
class AlarmConditionalFalse(Exception):
    def __init__(self):
        self.error = "If there is less than 5 minutes left for the alarm to go off, it cannot be changed or deleted."


class SlackChannelNotFound(Exception):
    def __init__(self):
        self.error = "Channel does not exist or cannot be found."
        
        
class AlarmMaximumTimeLimit(Exception):
    def __init__(self):
        self.error = "You can set up a reservation message in Slack for up to 4 months."
        

class InvalidDateSetting(Exception):
    def __init__(self):
        self.error = "If the interval is set, you can only enter the time."


class InvalidIntervalSetting(Exception):
    def __init__(self):
        self.error = "You cannot set an interval for an alarm with a date and time specified."
        

class DeadlineEarlierThanAlarmSet(Exception):
    def __init__(self):
        self.error = "Cannot set a deadline earlier than the current date."
        

class DeadlineNotSet(Exception):
    def __init__(self):
        self.error = "Alarm with no deadline set."
        

