from .ParameterOptimizer.ParameterOptimizer import DataGenerator
from .ImageEnhancer import ResizableEnhancer, Image
from .config import ImageInfo


class ImageGenerator(DataGenerator):
    def __init__(self, image_path: str):
        self.enhancer = ResizableEnhancer(image_path, ImageInfo.size)

    def generate(self, param: dict) -> Image:
        return self.enhancer.resized_enhance(param)
