from pathlib import Path


class ImageInfo:
    width, height, channel = shape = (224, 224, 3)
    size = (width, height)


class DirectoryPath:
    users = Path('volumes/users')
    optimizable = Path('volumes/optimizable')
