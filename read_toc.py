from PIL import Image
from pytesseract import *
from fabric.api import local
from os import listdir

def read_toc(filename, dir):
    local('convert -density 300 {1}/{0} {1}/output.png'.format(filename, dir))
    for f in [f for f in listdir(dir) if 'output' in f]:
        with open('toc.txt', 'a') as txt:
            txt.write(pytesseract.image_to_string(Image.open('{1}/{0}'.format(f, dir))))

read_toc('toc_math54.pdf', 'toc/54')
