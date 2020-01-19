import schedule
import time


def job():
    print('hello')


if __name__ == "__main__":
    schedule.every(5).seconds.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
