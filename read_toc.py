from PIL import Image
from pytesseract import *
from fabric.api import local
from os import listdir
from pdftools import pdf_add 


MAX_PAGE_RANGE = 25

def pdf_split(filename):
    local('touch dest.pdf')
    pdf_add('dest.pdf', filename,[1-MAX_PAGE_RANGE], None)

def read_toc(dir):
    filename = 'dest.pdf'
    local('convert -density 300 {1}/{0} {1}/output.png'.format(filename, dir))
    for f in [f for f in listdir(dir) if 'output' in f]:
        with open('toc.txt', 'a') as txt:
            txt.write(pytesseract.image_to_string(Image.open('{1}/{0}'.format(f, dir))))

pdf_split('toc_math54.pdf')
read_toc('toc/54')
