from pathlib import Path


class ImageInfo:
    width, height, channel = shape = (224, 224, 3)
    size = (width, height)


class DirectoryPath:
    weights = Path('volumes/weights')
    optimize = Path('volumes/optimize')
