import time
import datetime
import schedule


def job():
    print(datetime.datetime.now())


if __name__ == "__main__":
    schedule.every(10).seconds.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
