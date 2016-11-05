from PIL import Image
from pytesseract import *
from fabric.api import local
from os import listdir
from pdftools import pdf_add 

MIN_PAGE_RANGE = 1
MAX_PAGE_RANGE = 25
STARTER = 50

def pdf_split(filename, _min = MIN_RANGE_RANGE, _max=MAX_PAGE_RANGE):
    local('touch dest.pdf')
    pdf_add('dest.pdf', filename,[_min-_max], None)

def read(dir, output):
    filename = 'dest.pdf'
    local('convert -density 300 {1}/{0} {1}/output.png'.format(filename, dir))
    for f in [f for f in listdir(dir) if 'output' in f]:
        with open(output, 'a') as txt:
            txt.write(pytesseract.image_to_string(Image.open('{1}/{0}'.format(f, dir))))

pdf_split('toc_math54.pdf')
read('toc/54', 'toc.txt')

def offset(filename):
    pdf_split(filename, 50,50)
    read('toc/54', 'offset.txt')
    

