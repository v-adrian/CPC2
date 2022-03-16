# Superclass
class Question:
    def __init__(self):
        self._question = ""
        self._answer = ""

    def set_question(self, question):
        self._question = question

    def set_answer(self, answer):
        self._answer = answer

    def check_answer(self, response):
        return response == self._answer

    def display_question(self):
        print(self._question)

# Subclass
class MultipleChoice(Question):
    def __init__(self):
        super().__init__()
        self._choices = []

    def add_choice(self, choice, correct):
        self._choices.append(choice)
        if correct:
            choiceString = str(len(self._choices))
            self.set_answer(choiceString)

    def display_question(self):
        super().display_question()
        for i in range(len(self._choices)):
            choiceNumber = i + 1
            print("%d: %s" % (choiceNumber, self._choices[i]))
