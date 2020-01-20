from Enhancer.config import DirectoryPath
from .logger import logger


class User:
    def __init__(self):
        self.is_commited = False

    def recommit(self, user_name: str):
        self.is_commited = False
        self.commit(user_name)

    def commit(self, user_name: str):
        if self.is_commited:
            return

        user_dir = self.user_dir = DirectoryPath.users / user_name

        if not user_dir.exists():
            logger.warn(f'{str(user_dir)} is not exists !')
            return

        if not user_dir.is_dir():
            logger.warn(f'{str(user_dir)} is not directory !')
            return

        weight_dir = user_dir / 'weights'
        weight_file_path = weight_dir / 'weight.h5'
        self.weight_file_path = str(weight_file_path)

        if not weight_file_path.exists():
            logger.info(f'[{user_name}] weight file is nothing')
            return

        self.is_commited = True
