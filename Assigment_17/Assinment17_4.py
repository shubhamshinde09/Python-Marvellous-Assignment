import schedule
import time

def task4():
    print("Namaskar...")

schedule.every().day.at("09:00").do(task4)

while True:
    schedule.run_pending()
    time.sleep(1)
