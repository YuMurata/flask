from .ParameterOptimizer.ParameterOptimizer import BitDecoder
from .ImageEnhancer import enhance_name_list, MIN_PARAM, MAX_PARAM
import numpy as np


class ParamDecoder(BitDecoder):
    def decode(self, bit_list: list) -> dict:
        quantize_param_list = \
            np.array_split(bit_list, len(enhance_name_list))
        bit_size = len(quantize_param_list[0])

        decoded_param_list = \
            [int(''.join(map(str, list(quantize_param))), 2)
             for quantize_param in quantize_param_list]

        normalized_param_list = \
            [x*(MAX_PARAM-MIN_PARAM)/(2**bit_size-1)+MIN_PARAM
             for x in decoded_param_list]

        return dict(zip(enhance_name_list, normalized_param_list))
