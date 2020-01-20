from .ParameterOptimizer.ParameterOptimizer import PredictModel
from .ImageRankNet.ImageRankNet import RankNet
from PIL.Image import Image
from .config import ImageInfo


class PreferencePredictor(PredictModel):
    def __init__(self, model_weight_file_path: str):
        self.model = RankNet(ImageInfo.shape)
        self.model.load(model_weight_file_path)

    def predict(self, image: Image) -> float:
        return self.model.predict([image])[0][0]
