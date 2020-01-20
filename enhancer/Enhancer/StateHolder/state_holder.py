from .user import User
from .category import Category
from .image import Image


class StateHolder:
    def __init__(self):
        self.user = User()
        self.category = Category(self.user)
        self.image = Image(self.category)
