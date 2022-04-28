from re import I
from tkinter import *
from tkinter import ttk

import wordle_logic
import words
import database

# Declaring constants
BLACK = '#121213'
GRAY = '#3a3a3c'
YELLOW = '#b59f3b'
GREEN = '#538d4e'
WHITE = '#ffffff'
FONT = ('Roboto', '24', 'bold')


def new_game():
    global game
    game.grid_forget()
    game = wordle_logic.Wordle(root)


def show_scores():
    leaderboard_dict = database.show_scores()

    leaderboard_dialog = Toplevel(bg=BLACK)
    leaderboard_dialog.resizable(False, False)

    style = ttk.Style()
    style.theme_use('default')
    style.configure('Treeview',
                    background=BLACK,
                    foreground=WHITE,
                    rowheight=25,
                    fieldbackground=BLACK
                    )
    style.map('Treeview',
              background=[('selected', GRAY)]
              )

    leaderboard = ttk.Treeview(leaderboard_dialog)
    leaderboard['columns'] = ('player_name', 'player_tries', 'player_time')

    leaderboard.column('#0', width=0, stretch=NO)
    leaderboard.column('player_name', anchor=CENTER, width=80)
    leaderboard.column('player_tries', anchor=CENTER, width=80)
    leaderboard.column('player_time', anchor=CENTER, width=80)

    leaderboard.heading('#0', text="", anchor=CENTER)
    leaderboard.heading('player_name', text="Name", anchor=CENTER)
    leaderboard.heading('player_tries', text="Guessed in", anchor=CENTER)
    leaderboard.heading('player_time', text="Time taken (s)", anchor=CENTER)

    i = 0
    for key, value in sorted(leaderboard_dict.items(), key=lambda value: value[1][1], reverse=FALSE):
        leaderboard.insert(parent='', index='end', iid=i,
                           values=(str(key), value[0], value[1]))
        i += 1
    leaderboard.pack()


def import_custom_list():
    words.custom_list = True
    new_game()


def remove_scores():
    print('THIS WILL PERMANENTLY REMOVE ALL THE SCORES IN THE DATABASE, ARE YOU SURE?')
    while True:
        nuke_word = words.get_word().upper()
        confirmation = input(
            f'TYPE "{nuke_word}" TO CONFIRM, TYPE "CANCEL" TO CANCEL\n')
        if confirmation == 'CANCEL':
            break
        elif confirmation == f'{nuke_word}':
            database.remove_scores()
            break


root = Tk()
root.title('Wordle')
root.geometry('295x425')
root.resizable(False, False)
root.option_add('*tearOff', False)

menubar = Menu(root)
menu_game = Menu(menubar)
menu_options = Menu(menubar)
menu_advanced = Menu(menubar)

menubar.add_cascade(label='Game', menu=menu_game)
menu_game.add_command(label='New', command=new_game)
menu_game.add_command(label='Quit', command=root.quit)

menubar.add_cascade(label='Options', menu=menu_options)
menu_options.add_command(label='Scores', command=show_scores)
menu_options.add_command(label='Custom list',
                         command=import_custom_list)

menubar.add_cascade(label='Advanced', menu=menu_advanced)
menu_advanced.add_command(
    label='REMOVE ALL SCORES (PERMANENT)', command=remove_scores)


database.create_table()
game = wordle_logic.Wordle(root)

root.config(bg=BLACK, menu=menubar)
root.mainloop()
