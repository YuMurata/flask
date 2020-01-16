from . import config
from .oauth import drive
from .id_getter import get_folder_id, get_file_id, GDriveFileNotFoundException
from .exception import GDriveException
from pathlib import Path
from logger import Logger

logger = Logger(__name__)


class GDriveTimeoutException(GDriveException):
    pass


def upload_test():
    scored_param_dir_path = Path(config.root_scored_param_dir_path)
    for file_path in scored_param_dir_path.glob('**/scored_param.json'):

        folder_path = 'pydrive_test/'+str(file_path.parent)

        file_name = file_path.name

        folder_id = get_folder_id(folder_path, make_parents=True)
        metadata = {'parents': [{'id': folder_id}]}

        try:
            file_id = get_file_id(folder_id, file_name)
            metadata['id'] = file_id
        except GDriveFileNotFoundException:
            pass

        f = drive.CreateFile(metadata)

        f.SetContentFile(str(file_path))
        f['title'] = file_name

        f.Upload()

        logger.info(f'upload {file_name}')


def upload():
    try:
        scored_param_dir_path = Path(config.root_scored_param_dir_path)
        for file_path in scored_param_dir_path.glob('**/scored_param.json'):

            folder_path = str(file_path.parent)

            file_name = file_path.name

            folder_id = get_folder_id(folder_path, make_parents=True)
            metadata = {'parents': [{'id': folder_id}]}

            try:
                file_id = get_file_id(folder_id, file_name)
                metadata['id'] = file_id
            except GDriveFileNotFoundException:
                pass

            f = drive.CreateFile(metadata)

            f.SetContentFile(str(file_path))
            f['title'] = file_name

            f.Upload()

            logger.info(f'upload {file_name}')

    except TimeoutError:
        raise GDriveTimeoutException
