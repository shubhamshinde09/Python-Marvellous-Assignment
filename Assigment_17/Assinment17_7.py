import schedule
import time
import datetime

def backup():
    with open("backup_log.txt", "a") as file:
        file.write("Backup at: " + str(datetime.datetime.now()) + "\n")

schedule.every().hour.do(backup)

while True:
    schedule.run_pending()
    time.sleep(1)
