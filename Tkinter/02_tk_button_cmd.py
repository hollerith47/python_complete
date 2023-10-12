from tkinter import *

win = Tk()
win.geometry('400x400')
win.title('02_ With Tkinter')
win['bg']='cyan'
# label
label_01 = Label(win, text='Good Morning!', background='red', font=('verdana', 20, 'italic bold'), foreground='white')
label_01.place(x='100', y='100')

def Accepter():
    print("j'accepte")
    
def Refuser():
    print('je refuse')

# bouton
bouton_a = Button(win, text="Agree", bg= 'blue', fg='white', command=Accepter)
bouton_a.place(x='140', y='150')

bouton_d = Button(win, text="Disagree", bg= 'red', fg='white', command=Refuser)
bouton_d.place(x='220', y='150')


win.mainloop()