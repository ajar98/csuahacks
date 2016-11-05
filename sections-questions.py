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

    def __init__(self, parent-section, number):
        self.parent-section = parent-section
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


