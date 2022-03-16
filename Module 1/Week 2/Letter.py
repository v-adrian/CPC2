# Vonn Adrian C. Jutar - A121

class Letter:

    # Constructor that takes a sender and a recepient parameter
    def __init__(self, letterFrom, letterTo):
        self._sender = letterFrom
        self._recepient = letterTo
        self._lines = []

    # Method that adds a line to the body of the letter
    def addLine(self, line):
        self._lines.append(line)

    # Method that returns the text within the letter
    def getText(self):
        print(f'Dear {self._recepient}:\n')
        for line in self._lines:
            print(line)
        print()
        print('Sincerely,\n')
        print(self._sender)