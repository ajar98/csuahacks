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
    return (line_needed.split(" ")[-1].strip("\n") ,next_line.split(" ")[-1].strip("\n"))

