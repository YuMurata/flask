import schedule
import time
from Enhancer import optimize_all_user


if __name__ == "__main__":
    schedule.every(5).seconds.do(optimize_all_user)

    while True:
        schedule.run_pending()
        time.sleep(1)
