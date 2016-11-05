class Section():
    
    def __init__(self, chapter, number, questions=[]):
        self.number = number
        self.questions = questions
        self.reading = None
        self.chapter = None

    def number(self):
        return self.number

    def questions(self):
        return self.questions

    def add_questions(self, questions):
        for question in questions:
            self.questions.append(question)

class Question():

    def __init__(self, parent_section, number):
        self.parent_section = parent_section
        self.number = number
        self.text = None
        self.solution = None

    def display(self):
        return self.text

    def display_solution(self):
        return self.solution

def text_to_sections(text):
    sections = []
    for a in text:
        a = a.split(" ")
        if a[0].lower() == 'section':
            chapter = a[1].split(".")[0]
            num = a[1].split(".")[1]
            questions = text_to_questions(a[2:], num)
            sections += [Section(chapter, num, questions)]
    return sections

def text_to_questions(ques_num, parent_section):
    questions = []
    for num in ques_num:
        num = num.strip("\n")
        num = num.strip(",")
        num = num.strip(" ")
        num = num.strip(",")
        num = num.strip(".")
        num = int(num)
        questions+=[Question(parent_section, num)]
    
    return questions

def parse_string(_file):
    f = open(_file, 'r')
    return f.readlines()
