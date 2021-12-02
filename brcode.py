# pip install qrcode[pil]
# brew install zbar
# pip install pyzbar

from typing import List
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask
from pyzbar.pyzbar import decode as qrdecode
from PIL import Image
import io

class BRCode:
    def __init__(self):
        self.qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.qr.clear()

    def make_image(self, url, embeded_image):
        self.qr.add_data(url)
        self.img = self.qr.make_image(
            image_factory = StyledPilImage,
            module_drawer = RoundedModuleDrawer(),
            color_mask = SolidFillColorMask(back_color=(255, 255, 255), front_color=(208, 2, 0)),
            embeded_image_path = embeded_image
        )
        img_byte_arr = io.BytesIO()
        self.img.save(img_byte_arr)
        return img_byte_arr.getvalue()

    def save_image(self, image_path) -> None:
        self.img.save(image_path)

    def decode_image(self, input_image) -> list:
        return qrdecode(Image.open(input_image))
        