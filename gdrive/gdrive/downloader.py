from . import config
from .oauth import drive
from .id_getter import get_folder_id
from .exception import GDriveTimeoutException
from pathlib import Path
from logger import Logger

logger = Logger(__name__)


def recursive_download(parents_id: str, dest_folder_path: str):
    logger.debug(f'parents_id: {parents_id}')
    logger.debug(f'dest_folder_path: {dest_folder_path}')

    parents_query = f'"{parents_id}" in parents'
    untrashed_query = 'trashed = false'
    query = f'{parents_query} and {untrashed_query}'

    for f in drive.ListFile({'q': query}).GetList():
        logger.debug(f'f_name: {f["title"]} in {parents_id}')
        if f['mimeType'] == 'application/vnd.google-apps.folder':
            recursive_download(f['id'], str(Path(dest_folder_path)/f['title']))

        else:
            folder_path = Path(dest_folder_path)
            folder_path.mkdir(exist_ok=True, parents=True)

            file_path = str(Path(dest_folder_path)/f['title'])
            f.GetContentFile(file_path)
            logger.info(f'download {f["title"]} to {dest_folder_path}')


def download_test():
    try:
        folder_path = 'pydrive_test/'+str(config.root_weights_dir_path)
        folder_id = get_folder_id(folder_path)
        recursive_download(folder_id, 'weights')
    except TimeoutError:
        raise GDriveTimeoutException
