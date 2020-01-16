import os

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def local_chdir(func):
    def _inner(*args, **kwargs):
        # 元のカレントディレクトリを変数に代入
        dir_original = os.getcwd()
        # 渡された関数実行
        ret = func(*args, **kwargs)
        # カレントディレクトリを元に戻す
        os.chdir(dir_original)
        return ret
    return _inner


@local_chdir
def init_drive():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()

    return GoogleDrive(gauth)


drive = init_drive()
