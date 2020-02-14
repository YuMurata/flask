from . import (auth, compare, index, scored_data, image)
bp_list = [auth.auth_bp, compare.compare_bp, index.index_bp,
           scored_data.scored_data_bp, image.image_bp]
