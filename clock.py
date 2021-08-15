from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from os import environ
from twilio.rest import Client 

sched = BlockingScheduler()
account_sid = 'AC5e7d9b0bdf266ba786913630b8a0d8d4' 
auth_token = '201b9f8460882601cda85667d0427202'
client = Client(account_sid, auth_token) 

@sched.scheduled_job('cron', day_of_week='mon-sun',seconds=55, timezone='Asia/Kolkata')
def automate_message():
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body='Good Morning Rahul... Please take glass of warm water',      
                                to='whatsapp:+916205192178' 
                            ) 
    
    print(message.sid)()

sched.start()


