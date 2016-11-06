from PIL import Image
from pytesseract import *
from fabric.api import local
from os import listdir
from pdftools import pdf_add 

MIN_PAGE_RANGE = 1
MAX_PAGE_RANGE = 25
STARTER = 50

def pdf_split(filename, output, _min = MIN_PAGE_RANGE, _max=MAX_PAGE_RANGE):
    local('touch {0}'.format(output))
    local('convert -density 500 {0}[{1}-{2}] {3}'.format(filename, _min, _max, output))

def read(filename, dir, output):
    local('convert -density 500 {0} {1}/output.png'.format(filename, dir))
    for f in [f for f in listdir(dir) if 'output' in f]:
        with open(output, 'a') as txt:
            txt.write(pytesseract.image_to_string(Image.open('{1}/{0}'.format(f, dir))))
    local('rm -rf {0}/output*'.format(dir))

def read_toc(txtbook, dir, output, start_page, end_page):
    pdf_split('{0}'.format(txtbook), '{0}.pdf'.format(output), _min=start_page, _max=end_page)
    read('{0}.pdf'.format(output), dir, '{0}.txt'.format(output))

def offset(filename, dir, output):
    pdf_split(filename, '{0}/{1}.pdf'.format(dir, output), STARTER, STARTER)
    read('{0}/{1}.pdf'.format(dir, output), dir, '{0}/{1}.txt'.format(dir, output))
    with open('{0}/{1}.txt'.format(dir, output), 'r') as f:
        line = f.readline()
        page_number = None
        for token in line.split(' '):
            if token.isdigit():
                page_number = int(token)
                break
    return STARTER - page_number

# read_toc('pdfs/54/math54.pdf', 'pdfs/54', 'pdfs/toc', 5, 8)
# print(offset('pdfs/54/math54.pdf'))
