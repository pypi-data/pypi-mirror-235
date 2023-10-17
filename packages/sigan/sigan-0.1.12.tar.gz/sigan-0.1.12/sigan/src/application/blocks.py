def alarm_blocks(alarm: dict):
    blocks = [
		{
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": "The alarm has arrived!",
				"emoji": True
			}
		},
		{
			"type": "section",
			"fields": [
         		{
					"type": "mrkdwn",
					"text": f"*Content:*\n{alarm['content']}",
				},
        	    {
					"type": "mrkdwn",
					"text": f"*Deadline:*\n{alarm['deadline']}",
				},
				{
					"type": "mrkdwn",
					"text": f"*Notification Time:*\n{alarm['alarm_date']}",
				},
				{
					"type": "mrkdwn",
					"text": f"*Interval:*\n{alarm['interval']}"
				},
			]
		},
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "Are you sure you want to delete the alarm?",
				"emoji": True
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"emoji": True,
						"text": "Check"
					},
					"style": "primary",
					"value": "click_me_123"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"emoji": True,
						"text": "Delete"
					},
					"style": "danger",
					"value": "click_me_123"
				}
			]
		}
	]
    return blocks