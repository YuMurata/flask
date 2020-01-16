import config
from oauth import drive
from pathlib import Path
import re


class GDriveException(Exception):
    pass


class GDriveFolderNotFoundException(GDriveException):
    pass


class GDriveFileNotFoundException(GDriveException):
    pass


def get_folder_id(folder_path: str, make_parents: bool = False) -> str:
    parents_id = 'root'

    pattarn = re.escape(r'/\\')

    for folder_name in re.split(f'[{pattarn}]', folder_path):
        print(parents_id)
        print(folder_name)
        title_query = f'title = "{folder_name}"'
        parents_query = f'"{parents_id}" in parents'
        mimeType_query = 'mimeType = "application/vnd.google-apps.folder"'

        query = f'{title_query} and {parents_query} and {mimeType_query}'

        try:
            folder_id = drive.ListFile({'q': query}).GetList()[0]['id']
        except IndexError:
            if make_parents:
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
    query = f'{title_query} and {parents_query} and {mimeType_query}'

    try:
        file_id = drive.ListFile({'q': query}).GetList()[0]['id']
    except IndexError:
        raise GDriveFileNotFoundException

    return file_id


def upload():
    scored_param_dir_path = Path(config.root_scored_param_dir_path)
    for file_path in scored_param_dir_path.glob('**/scored_param.json'):

        folder_path = 'pydrive_test/'+str(file_path.parent)
        print(folder_path)
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

        print(f'{file_name} upload')


upload()
