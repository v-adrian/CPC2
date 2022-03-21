# Vonn Adrian C. Jutar - A121

from tkinter import *

root = Tk()
root.title('Phone')
root.iconbitmap('phone-icon.ico')
root.config(bg='BLACK')
root.resizable(False, False)

display = Entry(root, relief=FLAT, width=20, justify=CENTER,
                font=('Arial', 15), bg='BLACK', fg='WHITE')
display.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_press(number):
    current = display.get()
    display.delete(0, END)
    display.insert(0, str(current)+str(number))


def button_clear():
    display.delete(0, END)


def button_calling():
    newWindow = Toplevel(root)
    newWindow.geometry('340x340')
    newWindow.title('Phone')
    newWindow.iconbitmap('phone-icon.ico')
    newWindow.config(bg='BLACK')
    newWindow.resizable(False, False)

    avatar = PhotoImage(file='empty-avatar1.png')
    avatar_photo = Label(newWindow, image=avatar, bg='BLACK', relief=FLAT)
    avatar_photo.image = avatar  # Needs to be done to display the image correctly

    calling_number = "Couldn't call " + display.get() + '...'
    text = Label(newWindow, text=calling_number,
                 font=('Arial', 15), bg='BLACK', fg='WHITE')

    avatar_photo.pack(pady=35)
    text.pack(side=BOTTOM, pady=40)
    newWindow.after(3000, lambda: newWindow.destroy())


photo_phone = PhotoImage(file='phone-icon-40px.png',)
photo_backspace = PhotoImage(file='backspace-icon.png')

button_1 = Button(root, relief=FLAT, padx=20, pady=15,
                  text=1, command=lambda: button_press(1), font=('Arial', 13), fg='WHITE', bg='BLACK')
button_2 = Button(root, relief=FLAT, padx=20, pady=15,
                  text=2, command=lambda: button_press(2), font=('Arial', 13), fg='WHITE', bg='BLACK')
button_3 = Button(root, relief=FLAT, padx=20, pady=15,
                  text=3, command=lambda: button_press(3), font=('Arial', 13), fg='WHITE', bg='BLACK')
button_4 = Button(root, relief=FLAT, padx=20, pady=15,
                  text=4, command=lambda: button_press(4), font=('Arial', 13), fg='WHITE', bg='BLACK')
button_5 = Button(root, relief=FLAT, padx=20, pady=15,
                  text=5, command=lambda: button_press(5), font=('Arial', 13), fg='WHITE', bg='BLACK')
button_6 = Button(root, relief=FLAT, padx=20, pady=15,
                  text=6, command=lambda: button_press(6), font=('Arial', 13), fg='WHITE', bg='BLACK')
button_7 = Button(root, relief=FLAT, padx=20, pady=15,
                  text=7, command=lambda: button_press(7), font=('Arial', 13), fg='WHITE', bg='BLACK')
button_8 = Button(root, relief=FLAT, padx=20, pady=15,
                  text=8, command=lambda: button_press(8), font=('Arial', 13), fg='WHITE', bg='BLACK')
button_9 = Button(root, relief=FLAT, padx=20, pady=15,
                  text=9, command=lambda: button_press(9), font=('Arial', 13), fg='WHITE', bg='BLACK')
button_asterisk = Button(root, relief=FLAT, padx=20, pady=15,
                         text='*', command=lambda: button_press('*'), font=('Arial', 13), fg='WHITE', bg='BLACK')
button_0 = Button(root, relief=FLAT, padx=20, pady=15,
                  text=0, command=lambda: button_press(0), font=('Arial', 13), fg='WHITE', bg='BLACK')
button_hashtag = Button(root, relief=FLAT, padx=20, pady=15,
                        text='#', command=lambda: button_press('#'), font=('Arial', 13), fg='WHITE', bg='BLACK')
button_call = Button(root, relief=FLAT, padx=20, pady=15,
                     image=photo_phone, command=lambda: button_calling(), font=('Arial', 13), fg='WHITE', bg='BLACK')
button_backspace = Button(root, relief=FLAT, padx=20, pady=15,
                          image=photo_backspace, command=lambda: button_clear(), font=('Arial', 13), fg='WHITE', bg='BLACK')

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_asterisk.grid(row=4, column=0)
button_0.grid(row=4, column=1)
button_hashtag.grid(row=4, column=2)
button_call.grid(row=5, column=1)
button_backspace.grid(row=5, column=2)

root.mainloop()

# Vonn Adrian C. Jutar - A121
