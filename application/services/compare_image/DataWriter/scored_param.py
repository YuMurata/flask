import json
from pathlib import Path
import typing
import application.services.compare_image.Tournament.Tournament as Tournament

PlayerList = typing.List[Tournament.Player]


class ScoredParamWriterException(Exception):
    pass


SUFFIX = '.json'
root_save_dir_path = Path(r'./scored_param')


def write(save_file_path: str, player_list: PlayerList):
    if Path(save_file_path).suffix != SUFFIX:
        raise ScoredParamWriterException(f'suffix is not {SUFFIX}')

    save_list = [player.to_dict() for player in player_list]

    with open(save_file_path, 'w') as fp:
        json.dump(save_list, fp, indent=4)
