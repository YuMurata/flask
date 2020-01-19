from .param_decoder import ParamDecoder
from .image_generator import ImageGenerator
from .preference_predictor import PreferencePredictor
from .ParameterOptimizer.ParameterOptimizer import Optimizer
from .config import DirectoryPath
from .logger import Logger

logger = Logger(__name__)


def optimize_image():
    for user_dir in DirectoryPath.users.iterdir():
        if not user_dir.is_dir():
            logger.warn(f'{str(user_dir)} is not directory !')
            continue

        user_name = user_dir.name

        weight_dir = user_dir/'weights'
        weight_file_path = weight_dir/'weight.h5'

        optimize_dir = user_dir/'optimizes'
        optimize_dir.mkdir(exist_ok=True, parents=True)

        scored_param_dir = user_dir/'scored_param'

        generator = ImageGenerator(image_path)
        image_path = None
        param_list, logbook = \
            Optimizer(PreferencePredictor(model_weight_file_path),
                      generator,
                      ParamDecoder()).optimize(30, param_list_num=1)

        save_file_path = DirectoryPath.optimize
        generator.generate(param_list[0]).save()
        print(param_list)
