import schedule
import time
import datetime

def task2():
    print("Current time:", datetime.datetime.now())

schedule.every(1).minutes.do(task2)

while True:
    schedule.run_pending()
    time.sleep(1)
