import time
import schedule
from gdrive.exception import GDriveTimeoutException
from gdrive.uploader import upload_test
from gdrive.downloader import download_test

from logger import Logger

logger = Logger(__name__)


def upload_job():
    def insurance():
        try:
            upload_test()
            return schedule.CancelJob
        except GDriveTimeoutException:
            logger.warn('timeout upload. upload after 10 minutes')

    try:
        upload_test()
    except GDriveTimeoutException:
        logger.warn('timeout upload. upload after 10 minutes')
        schedule.every(10).minutes.do(insurance)


if __name__ == "__main__":
    schedule.every(5).seconds.do(upload_job)

    while True:
        schedule.run_pending()
        time.sleep(1)
