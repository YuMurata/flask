from .param_decoder import ParamDecoder
from .image_generator import ImageGenerator
from .preference_predictor import PreferencePredictor
from .ParameterOptimizer.ParameterOptimizer import Optimizer
from .config import DirectoryPath


def optimize_image():
    for user_dir in DirectoryPath.weights.iterdir()
    user_name = user_dir
    model_weight_file_path = None

    generator = ImageGenerator(image_path)
    image_path = None
    param_list, logbook = \
        Optimizer(PreferencePredictor(model_weight_file_path),
                  generator,
                  ParamDecoder()).optimize(30, param_list_num=1)

    save_file_path = DirectoryPath.optimize
    generator.generate(param_list[0]).save()
    print(param_list)
