from page_range import parser, page_range
from read import read_toc, offset, pdf_split
import sections-questions.py

text_pdf = ""
assignment_pdf = ""

assignment_txt = ""

#######################

index_pdf = ""
index_txt = ""

#######################

# offset_val = offset("")
offset_val = 16

toc_lines = parser(index_txt)
assignment_lines = parser(assignment_txt)
_sections = text_to_sections(assignment_lines)
p_ranges = []

for section in _sections:
    chapter, section_num = section.chapter, section.section_num
    p_ranges += [page_range(index_txt, chapter, section_num)]

page_min, page_max = page_range(parser('pdfs/toc.txt'), 6, 5)
page_min, page_max = int(page_min) + offset_val, int(page_max) + offset_val
pdf_split('pdfs/54/math54.pdf', 'least_squares.pdf', _min=page_min, _max=page_max)


