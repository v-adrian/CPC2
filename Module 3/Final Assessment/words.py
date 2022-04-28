from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import random

word_file = 'wordlist.txt'
custom_list = False


def get_word():
    global custom_list
    empty_list = ['EMPTY']
    word_list = []

    if custom_list == False:
        try:
            with open(word_file, 'r') as file:
                for line in file:
                    line = line.rstrip()
                    if "".join(dict.fromkeys(line)) == line and len(line) == 5:
                        word_list.append(line)

        except:
            messagebox.showerror(title='Error!', message='File not found.')

    if custom_list == True:
        custom_list = False
        import_word_list()

    if len(word_list) > 0:
        return random.choice(word_list)
    else:
        return empty_list[0]


def import_word_list():
    global word_file

    try:
        file = askopenfilename(title='Choose your list',
                               filetypes=(
                                   ('Text Documents', '*.txt'),
                               ))

        if len(file) > 0:
            word_file = file
        else:
            word_file = 'wordlist.txt'

    except:
        word_file = 'wordlist.txt'
