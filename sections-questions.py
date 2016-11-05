class Section():
    
    def __init__(self, number):
        self.number = number
        self.questions = []
        self.reading = None

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
        self.parent = number
        self.text = None
        self.solution = None

    def display(self):
        return self.text

    def display_solution(self):
        return self.solution

def text_to_sections(text):
    return

def text_to_questions(text):
    return

def parse_string(_file):
    f = open(_file, 'r')
    a = f.readlines()
