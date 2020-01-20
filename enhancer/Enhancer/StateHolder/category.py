from Enhancer.config import DirectoryPath
from .logger import logger
from .user import User


class Category:
    def __init__(self, user: User):
        self.is_commited = False
        self.user = user

    def recommit(self, user_name: str, category_name: str):
        self.is_commited = False
        self.commit(user_name, category_name)

    def commit(self, user_name: str, category_name: str):
        if self.is_commited:
            return

        self.user.commit(user_name)
        if not self.user.is_commited:
            return

        user_dir = self.user.user_dir

        scored_param_dir = user_dir / 'scored_params'
        scored_param_name_list = \
            [file_path.stem for file_path in scored_param_dir.iterdir()]

        if category_name not in scored_param_name_list:
            logger.info(f'[{user_name}] {category_name} is not scoring')

        category_dir = DirectoryPath.optimizable / category_name
        self.category_dir = category_dir
        if not category_dir.exists():
            logger.warn(f'{str(category_dir)} is not exists !')

        self.is_commited = True
