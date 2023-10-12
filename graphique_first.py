
from tkinter import *

root = Tk() #создание главного окна
btn = Button(root, text ='Кнопчка', width=10, 
             height=2, bg= "blue", fg="black", font="Tahoma_12")
lab = Label(root, text ="Enter your Name", font="Tahoma_14")
Edit =Entry(root, width=15)
btn.pack()
lab.pack()
Edit.pack()
root.mainloop()


