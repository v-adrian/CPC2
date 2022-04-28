from tkinter import *
import time

import words
import database

# Declaring constants
BLACK = '#121213'
GRAY = '#3a3a3c'
YELLOW = '#b59f3b'
GREEN = '#538d4e'
WHITE = '#ffffff'
FONT = ('Roboto', '24', 'bold')


class Wordle(Frame):
    _guess_num = 0
    _guess_time = 0

    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.config(self, bg=BLACK)
        self.grid(row=8, column=0, columnspan=5)

        global word_to_guess
        words.get_word()
        word_to_guess = words.get_word().upper()
        # line below for debugging purposes, comment out to have a real game
        # print(word_to_guess)

        global number_of_tries
        number_of_tries = Label(self, text=str(6-self._guess_num)+'/6', bg=BLACK, fg=WHITE, font=FONT,
                                justify=CENTER, relief=FLAT)
        number_of_tries.grid(row=9, column=0, columnspan=5)

        global word_input
        word_input = Entry(self, bg=GRAY, bd=1, fg=WHITE, font=FONT,
                           justify=CENTER, relief=FLAT, width=15)
        word_input.bind(
            '<Return>', self.word_guess)
        word_input.grid(row=8, column=0, columnspan=5, padx=10, pady=10)

        global start
        start = time.time()

    def word_guess(self, guess):
        guess = word_input.get()
        guess = guess.upper()
        word_input.delete(0, END)

        if self._guess_num < 6:

            if guess.isalpha() and len(guess) == 5:
                self._guess_num += 1
                number_of_tries.config(text=str(6-self._guess_num)+'/6')

                if guess == word_to_guess:
                    for i, letter in enumerate(guess):
                        label = Label(self, text=letter.upper(),
                                      bg=GREEN, fg=WHITE, font=FONT, width=2)
                        label.grid(row=self._guess_num+1,
                                   column=i, padx=5, pady=5)
                    word_input.config(
                        state=DISABLED, disabledbackground=GRAY)
                    self._guess_time = f'{time.time() - start:.2f}'
                    self.save_score()
                else:
                    for i, letter in enumerate(guess):
                        label = Label(self, text=letter.upper(),
                                      bg=BLACK, fg=WHITE, font=FONT)
                        label.grid(row=self._guess_num+1,
                                   column=i, padx=5, pady=5)

                        if letter == word_to_guess[i]:
                            label.config(bg=GREEN, width=2)

                        elif letter in word_to_guess:
                            label.config(bg=YELLOW, width=2)

                        else:
                            label.config(bg=GRAY, width=2)

        else:
            word_input.config(state=DISABLED, disabledbackground=GRAY)

    def save_score(self):

        save_dialog = Toplevel(bg=BLACK)
        save_dialog.resizable(False, False)

        if self._guess_num == 1:
            tries = 'try.'
        else:
            tries = 'tries.'
        congrats = Label(save_dialog, text=f'You took {self._guess_time} seconds to answer and \nyou got it in {self._guess_num} {tries}', bg=BLACK, fg=WHITE, font=FONT,
                         justify=CENTER, relief=FLAT)
        player_name = Label(save_dialog, text='NAME:', bg=BLACK, fg=WHITE, font=FONT,
                            justify=CENTER, relief=FLAT)
        player_name_entry = Entry(save_dialog, bg=GRAY, bd=1, fg=WHITE, font=FONT,
                                  justify=CENTER, relief=FLAT, width=10)
        submit = Button(save_dialog, text='Submit', bg=GRAY, bd=1, fg=WHITE, font=FONT,
                        justify=CENTER, relief=FLAT, width=18, command=lambda: [database.save_score(player_name_entry.get().upper(), self._guess_num, self._guess_time), save_dialog.destroy()])

        congrats.grid(row=0, column=0, columnspan=2)
        player_name.grid(row=1, column=0, padx=15, pady=5)
        player_name_entry.grid(row=1, column=1, padx=10, pady=5)
        submit.grid(row=2, column=0, columnspan=2, padx=10, pady=5)
