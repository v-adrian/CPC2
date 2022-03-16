from tkinter import *

root = Tk()
root.resizable(width=False, height=False)
root.title('Exercise #4 - Myself')

my_photo = PhotoImage(file='picture.gif')
picture = Label(root, image=my_photo, relief=GROOVE, width=250, height=250)
picture.grid(row=0, column=0)

text = Label(root, relief=GROOVE, text='Vonn Adrian C. Jutar\nGeneral Santos City, October 2001', font=(
    'Arial', 16, 'bold', 'italic'), fg='#ffffff', bg='#ff58c2')
text.grid(row=0, column=1)

root.mainloop()
