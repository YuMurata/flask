import json
from pathlib import Path
from application.services.compare import Tournament


class ScoredParamWriterException(Exception):
    pass


SUFFIX = '.json'
root_save_dir_path = Path(r'./scored_param')
file_name = f'scored_param{SUFFIX}'


def write(save_file_path: str, player_list: Tournament.PlayerList):
    if Path(save_file_path).suffix != SUFFIX:
        raise ScoredParamWriterException(f'suffix is not {SUFFIX}')

    save_list = [player.to_dict() for player in player_list]

    with open(save_file_path, 'w') as fp:
        json.dump(save_list, fp, indent=4)


def get_save_dir_path(user_name: str, image_name: str) -> Path:
    save_dir_path = root_save_dir_path/user_name/image_name
    save_dir_path.mkdir(parents=True, exist_ok=True)

    return save_dir_path


def get_save_file_path(user_name: str, image_name: str) -> Path:
    save_dir_path = get_save_dir_path(user_name, image_name)
    save_file_path = save_dir_path/file_name

    return save_file_path
