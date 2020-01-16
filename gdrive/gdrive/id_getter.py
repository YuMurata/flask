from .oauth import drive
from .exception import GDriveException

import re
from logger import Logger

logger = Logger(__name__)


class GDriveFolderNotFoundException(GDriveException):
    pass


class GDriveFileNotFoundException(GDriveException):
    pass


def get_folder_id(folder_path: str, make_parents: bool = False) -> str:
    parents_id = 'root'

    pattarn = re.escape(r'/\\')

    for folder_name in re.split(f'[{pattarn}]', folder_path):
        logger.debug(f'parents_id: {parents_id}')
        logger.debug(f'folder_name: {folder_name}')

        title_query = f'title = "{folder_name}"'
        parents_query = f'"{parents_id}" in parents'
        mimeType_query = 'mimeType = "application/vnd.google-apps.folder"'
        untrashed_query = 'trashed = false'

        query = ' and '.join(
            [title_query, parents_query, mimeType_query, untrashed_query])

        try:
            folder_id = drive.ListFile({'q': query}).GetList()[0]['id']
        except IndexError:
            if make_parents:
                logger.info(f'make {folder_name} in {parents_id}')

                f_folder = drive.CreateFile({
                    'title': folder_name,
                    'mimeType': 'application/vnd.google-apps.folder',
                    'parents': [{'id': parents_id}]})

                f_folder.Upload()

                f_folder.FetchMetadata()
                folder_id = f_folder['id']

            else:
                raise GDriveFolderNotFoundException

        parents_id = folder_id

    return parents_id


def get_file_id(folder_id: str, file_name: str) -> str:
    title_query = f'title = "{file_name}"'
    parents_query = f'"{folder_id}" in parents'
    mimeType_query = 'mimeType != "application/vnd.google-apps.folder"'
    untrashed_query = 'trashed = false'

    query = ' and '.join(
            [title_query, parents_query, mimeType_query, untrashed_query])

    try:
        file_id = drive.ListFile({'q': query}).GetList()[0]['id']
    except IndexError:
        raise GDriveFileNotFoundException

    return file_id
