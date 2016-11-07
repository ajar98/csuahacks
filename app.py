from page_range import parser, page_range
from read import read, read_toc, offset, pdf_split
from sections_questions import *
import sys
from fabric.api import local

if __name__ == '__main__':
    dir = sys.argv[1]
    text_pdf = sys.argv[2]
    assignment_txt = sys.argv[3]
    
    print('Dir: {0}, PDF file: {1}, Assignment file: {2}'.format(dir, text_pdf, assignment_txt))

#######################

    index_txt = '{0}/toc'.format(dir)
    read_toc(text_pdf, dir, index_txt, 5, 8)


#######################

    offset_val = offset(text_pdf, '{0}/offset'.format(dir), 'offset')

    print('Offset: {0}'.format(offset_val))

    toc_lines = parser('{0}.txt'.format(index_txt))
    assignment_lines = parser(assignment_txt)
    _sections = text_to_sections(assignment_lines)

    for section in _sections:
        chapter, section_num = section.chapter, section.number
        page_min, page_max = page_range(toc_lines, chapter, section_num)
        page_min, page_max = int(page_min) + offset_val, int(page_max) + offset_val
        pdf_split(text_pdf, 'hw.pdf', _min=page_min, _max=page_max)

    local('open hw.pdf')
