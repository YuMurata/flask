import time
import datetime
import schedule
from oauth import drive


def job():
    print(datetime.datetime.now())


if __name__ == "__main__":
    schedule.every(5).seconds.do(upload)
    while True:
        schedule.run_pending()
        time.sleep(1)
