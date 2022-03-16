# Vonn Adrian C. Jutar - A121
# Testing Letter.py

from Letter import Letter

letter = Letter('Mary', 'John')

letter.addLine('I am sorry we must part.')
letter.addLine('I wish you all the best.')
letter.getText()

# Test 2
letter2 = Letter('John','Mary')

letter2.addLine(f'It is unfortunate for us to part, {letter2._sender}.')
letter2.addLine('Hopefully, I shall see you again.')
letter2.getText()
