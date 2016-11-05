from PIL import Image
from pytesseract import *

print(pytesseract.image_to_string(Image.open('toc_math54/page-0.jpg')))
