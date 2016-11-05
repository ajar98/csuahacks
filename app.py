from page_range import parser, page_range
from read import read_toc, offset, pdf_split

offset = 16

page_min, page_max = page_range(parser('pdfs/toc.txt'), 6, 5)
page_min, page_max = int(page_min) + 16, int(page_max) + 16
pdf_split('pdfs/54/math54.pdf', 'least_squares.pdf', _min=page_min, _max=page_max)

