from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from message import automate_message

sched = BlockingScheduler()

#sched.add_job(automate_message,'interval',hour=2)      # if you want to send send message in every 2 hours 
#sched.add_job(automate_message, 'date', run_date='2021-07-31 21:40:00')     # if you want to send send message at specific date and time
sched.add_job(automate_message,'cron',day_of_week='mon-sun',hour=5, minute=10 )

sched.start()