# Vonn Adrian C. Jutar - A121
# Testing Question.py

from Question import *

# Adding the questions and choices
def main():
    first = MultipleChoice()
    first.set_question("1x1")
    first.add_choice("1", True)
    first.add_choice("0", False)
    first.add_choice("-1", False)
    first.add_choice("11", False)

    second = MultipleChoice()
    second.set_question("2x2")
    second.add_choice("22", False)
    second.add_choice("4", True)
    second.add_choice("8", False)
    second.add_choice("16", False)

    third = MultipleChoice()
    third.set_question("3x3")
    third.add_choice("6", False)
    third.add_choice("12", False)
    third.add_choice("27", False)
    third.add_choice("9", True)

    fourth = MultipleChoice()
    fourth.set_question("4x4")
    fourth.add_choice("12", False)
    fourth.add_choice("8", False)
    fourth.add_choice("16", True)
    fourth.add_choice("-16", False)

    fifth = MultipleChoice()
    fifth.set_question("5x5")
    fifth.add_choice("25", True)
    fifth.add_choice("-10", False)
    fifth.add_choice("10", False)
    fifth.add_choice("-25", False)

    show_question(first)
    show_question(second)
    show_question(third)
    show_question(fourth)
    show_question(fifth)

# Displays the questions and checks whether the answer is correct
def show_question(Question):
    Question.display_question()
    response = input("Your answer: ")
    print(Question.check_answer(response))

main()
