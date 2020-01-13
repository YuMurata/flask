from pathlib import Path

image_dir_path = Path(r'./application/static/images')

image_path_dict = {image_path.stem: image_path
                   for image_path in image_dir_path.iterdir()}
