from .param_decoder import ParamDecoder
from .image_generator import ImageGenerator
from .preference_predictor import PreferencePredictor
from .ParameterOptimizer.ParameterOptimizer import Optimizer
from .config import DirectoryPath, Path
import pickle
from .StateHolder import StateHolder
from .logger import Logger

logger = Logger(__name__, log_file_path='logs/optimize.log')


def optimize_image(user_name: str, category_name: str, image_path: str,
                   state_holder: StateHolder):
    state_holder.image.recommit(user_name, category_name, image_path)
    if not state_holder.image.is_commited:
        return

    user_dir = state_holder.user.user_dir
    weight_file_path = state_holder.user.weight_file_path

    generator = ImageGenerator(image_path)
    param_list, logbook = \
        Optimizer(PreferencePredictor(weight_file_path),
                  generator,
                  ParamDecoder()).optimize(30, param_list_num=1,
                                           verbose=False)

    image_name = state_holder.image.image_name

    optimizes_dir = user_dir / 'optimizes'

    image_save_dir = optimizes_dir / category_name
    image_save_dir.mkdir(exist_ok=True, parents=True)
    image_save_file_path = str(image_save_dir / image_name)

    generator.generate(param_list[0]).save(image_save_file_path)

    logbook_dir = image_save_dir / 'logs'
    logbook_dir.mkdir(exist_ok=True, parents=True)
    logbook_file_path = str(logbook_dir / image_name)

    with open(logbook_file_path, 'w') as fp:
        pickle.dump(logbook, fp)

    logger.info(f'[{user_name}] optimize {image_name} in {category_name}')


def optimize_category_image(user_name: str, category_name: str,
                            state_holder: StateHolder):

    state_holder.category.recommit(user_name, category_name)
    if not state_holder.category.is_commited:
        return

    category_dir = state_holder.category.category_dir
    for image_path in category_dir.iterdir():
        optimize_image(user_name, category_name, str(image_path), state_holder)

    logger.info(f'[{user_name}] optimize all image in {category_name}')


def optimize_user(user_name: str, state_holder: StateHolder):
    state_holder.user.recommit(user_name)
    if not state_holder.user.is_commited:
        return

    for category_dir in DirectoryPath.optimizable.iterdir():
        optimize_category_image(user_name, category_dir.name, state_holder)

    logger.info(f'[{user_name}] optimize all image')


def optimize_all_user():
    for user_dir in DirectoryPath.users.iterdir():
        optimize_user(user_dir.name, StateHolder())

    logger.info('optimize all user')
