from .param_decoder import ParamDecoder
from .image_generator import ImageGenerator
from .preference_predictor import PreferencePredictor
from .ParameterOptimizer.ParameterOptimizer import Optimizer
from .config import DirectoryPath, Path
from .logger import Logger

logger = Logger(__name__)


def optimize_category_image(category_dir: Path, weight_file_path: str,
                            optimizes_dir: Path):
    for image_path in category_dir.iterdir():
        if image_path.is_dir():
            logger.warn(f'{str(image_path)} is directory !')
            continue

        generator = ImageGenerator(str(image_path))
        param_list, logbook = \
            Optimizer(PreferencePredictor(weight_file_path),
                      generator,
                      ParamDecoder()).optimize(30, param_list_num=1,
                                               verbose=False)

        save_dir = optimizes_dir / category_dir.name
        save_dir.mkdir(exist_ok=True, parents=True)
        save_file_path = str(save_dir / image_path.name)

        generator.generate(param_list[0]).save(save_file_path)


def optmize_all_category_image(scored_param_name_list: list, user_dir: Path,
                               weight_file_path: str):
    optimizes_dir = user_dir / 'optimizes'

    for category_dir in DirectoryPath.optimizable.iterdir():
        if not category_dir.is_dir():
            logger.warn(f'{str(category_dir)} is not directory !')
            continue

        if category_dir.name not in scored_param_name_list:
            logger.debug(
                f'[{user_dir.name}] {category_dir.name} is not scoring')
            continue

        optimize_category_image(category_dir, weight_file_path, optimizes_dir)

    logger.info(f'optimize all user')


def optimize_all_user():
    for user_dir in DirectoryPath.users.iterdir():
        if not user_dir.is_dir():
            logger.warn(f'{str(user_dir)} is not directory !')
            continue

        user_name = user_dir.name

        weight_dir = user_dir / 'weights'
        weight_file_path = weight_dir / 'weight.h5'
        if not weight_file_path.exists():
            logger.debug(f'[{user_name}] weight file is nothing')
            continue

        scored_param_dir = user_dir / 'scored_param'
        scored_param_name_list = [
            file_path.stem for file_path in scored_param_dir.iterdir()]

        optmize_all_category_image(
            scored_param_name_list, user_name, str(weight_file_path))

    logger.info('optimize all user')
