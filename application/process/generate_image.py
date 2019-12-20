from PIL.Image import Image
import io
import base64


def enhance(param) -> Image:
    pass


def to_base64(image: Image):

    output = io.BytesIO()
    image.save(output, format='PNG')

    base64_image = base64.b64encode(
        output.getvalue()).decode().replace("'", "")

    return 'data:image/png;base64,'+base64_image
