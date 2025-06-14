import schedule
import time

def task3():
    print("Do Coding..!")

schedule.every(30).minutes.do(task3)

while True:
    schedule.run_pending()
    time.sleep(1)
