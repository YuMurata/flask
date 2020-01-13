from .ImageEnhancer import ImageEnhancer
import io
import base64


class EnhanceEncoder:
    def __init__(self, image_path: str):
        self.enhancer = ImageEnhancer(image_path)

    def Encode(self, param):
        image = self.enhancer.enhance(param)

        output = io.BytesIO()
        image.save(output, format='PNG')

        base64_image = base64.b64encode(
            output.getvalue()).decode().replace("'", "")

        return 'data:image/png;base64,'+base64_image
