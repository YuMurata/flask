from pathlib import Path
from .logger import logger
from .category import Category


class Image:
    def __init__(self, category: Category):
        self.is_commited = False
        self.category = category

    def recommit(self, user_name: str, category_name: str, image_path: str):
        self.is_commited = False
        self.commit(user_name, category_name, image_path)

    def commit(self, user_name: str, category_name: str, image_path: str):
        if self.is_commited:
            return

        self.category.commit(user_name, category_name)
        if not self.category.is_commited:
            return

        image_path = Path(image_path)
        self.image_name = image_path.name

        if not image_path.exists():
            logger.warn(f'{str(image_path)} is not exists !')
            return

        if image_path.is_dir():
            logger.warn(f'{str(image_path)} is directory !')
            return

        self.is_commited = True
