from tkinter import *

win = Tk()
win.geometry('400x400')
win.title('Debut avec Tkinter')
win['bg']= 'blue'
# win.resizable(height=False, width=False)

label = Label(win, text="Hmak47", background='red')
# label.pack(side=RIGHT, padx=100)
label.place(x='100', y='0')

win.mainloop()