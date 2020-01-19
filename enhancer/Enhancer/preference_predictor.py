from ParameterOptimizer.ParameterOptimizer import PredictModel
from ImageRankNet.ImageRankNet import RankNet
from PIL.Image import Image
from .config import IMAGE_SHAPE


class PreferencePredictor(PredictModel):
    def __init__(self, model_weight_file_path: str):
        self.model = RankNet(IMAGE_SHAPE)
        self.model.load(model_weight_file_path)

    def predict(self, image: Image) -> float:
        return self.model.predict([image])[0][0]
