from tkinter import *
import webbrowser

def open_youtube():
    webbrowser.open_new('www.youtube.ru')

win = Tk()
win.title('Frame in Tk')
win.geometry('540x364')
win.minsize(300,200)
win.iconbitmap('logo1.ico')
win.config(bg='#229fe0')

# creer la frame  attention bd= border
frame = Frame(win, bg='#229fe0', bd=1)

# premier titre
label_title = Label(frame, text='Welcome to my Python Application', bg='#229fe0', font=('Verdana', 18, 'bold'))
label_title.pack()

# deuxieme titre
label_subtitle = Label(frame, text= "Hello word, I'm Hmak47", bg='#229fe0', font=('Verdana', 10, 'bold'))
label_subtitle.pack()

# Bouton lien vers youtube
yt_button = Button(frame, text="Open Youtube", font=('Courrier', 20, 'bold'), bg='white', fg='#229fe0', command=open_youtube)
# attention ici on a ajouter du padding dans le button avec pady
yt_button.pack(pady=15, fill=X)

# afficher le frame
frame.pack(expand=YES)




win.mainloop()