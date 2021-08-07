from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from message import automate_message



sched = BlockingScheduler()

# Schedule job_function to be called every two hours
#sched.add_job(automate_message, 'date', run_date='2021-07-31 21:40:00')
#sched.add_job(automate_message, 'date', run_date=datetime(2021, 8, 2, 17, 10 , 5))
sched.add_job(automate_message,'cron',day_of_week='mon-fri',hour=6, minute=50 )

sched.start()