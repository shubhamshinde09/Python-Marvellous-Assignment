
import schedule
import time
import datetime

def task5():
    with open("Marvellous.txt", "a") as file:
        file.write(str(datetime.datetime.now()) + "\n")

schedule.every(5).minutes.do(task5)

while True:
    schedule.run_pending()
    time.sleep(1)
