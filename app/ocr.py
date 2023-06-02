import pathlib,pytesseract
from PIL import Image

BASE_DIR=pathlib.Path(__file__).parent
IMG_DIR=BASE_DIR/"images"
IMG_PATH=IMG_DIR/"test.png"

img=Image.open(IMG_PATH)
print(pytesseract.image_to_string(img))