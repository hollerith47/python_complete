from tkinter import *

win = Tk()
win.geometry('500x500')
win.title('Input with Tkinter')
win['bg'] = '#aa5b4d'
win.resizable(height=False, width=False)

# label
label_01 = Label(win, text='Good Morning!', background='red', font=('verdana', 20, 'italic bold'), foreground='white')
label_01.place(x='140', y='160')


def Accepter():
    if mayo_imia.get() == 'Hmak':
        print("demande acceptee")
    else:
        print("it is not you!")

def Refuser():
    print('je refuse')


# bouton
bouton_a = Button(win, text="Valider", bg='blue', fg='white', command=Accepter)
bouton_a.place(x='180', y='270')

bouton_d = Button(win, text="Annuler", bg='red', fg='white', command=Refuser)
bouton_d.place(x='260', y='270')

mayo_imia= StringVar()
imia = Entry(win, textvariable= mayo_imia)
imia.place(x='190', y='230')









win.mainloop()