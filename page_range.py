def parser(text):
    f = open(text, 'r')
    lines = f.readlines()
    while('\n' in lines):
        lines.remove('\n')          ###Remove a bunch of new lines
    return lines

def page_range(lines, chapter, section_num):
    line_needed, next_line = None, None
    for i in range(len(lines)):
        line = lines[i].split(" ")
        first = line[0]
        if "." in first:
            chap, num = first.split(".")
            if int(chap) == chapter and int(num) == section_num:
                line_needed, next_line = lines[i], lines[i+1]
                break
    
    first_line, second_line = line_needed.split(" "), next_line.split(" ")
    if len(first_line) <= 1:
        a,_ = page_range(lines, chapter-1, section_num)
        _,b = page_range(lines, chapter+1, section_num)
        return a,b, chapter, section_num
    return (first_line[-1].strip("\n") , second_line[-1].strip("\n"))

