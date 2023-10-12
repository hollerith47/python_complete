import string
from random import randint, choice
from tkinter import *


def generate_password():
    password_min = 6
    password_max = 12
    all_chars = string.ascii_letters + string.punctuation + string.digits
    
    password = "".join(choice(all_chars) for _ in range(randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(10, password)


win = Tk()
win.title("Password Generator")
win.geometry('630x350')
win.resizable(height=False, width=False)
win.iconbitmap('logo1.ico')
win.config(bg='#229fe0')

# creation frame principale
frame = Frame(win, bg="#229fe0")
frame.pack(expand=YES)

# image creation
width = height = 300
image = PhotoImage(file="password.png").zoom(28).subsample(50)
canvas = Canvas(frame, width=width, height=height, bg='#229fe0', bd=0, highlightthickness=0)
canvas.create_image(width / 2, height / 2, image=image)
canvas.grid(row=0, column=0, sticky=W)

# creation sous boite
right_frame = Frame(frame, bg='#229fe0')
right_frame.grid(row=0, column=1, sticky=W)

# titre
label_title = Label(right_frame, text="Password", font=('Helvetica', 20), bg='#229fe0', fg='white')
label_title.pack()

# champs d input
password_entry = Entry(right_frame, font=('Helvetica', 20), bg='#229fe0', fg='white', width=13)
password_entry.pack()

# titre
generate_password_button = Button(right_frame, text="Generate", font=('Helvetica', 20),
                                  bg='#921a53', fg='white', command=generate_password)
generate_password_button.pack(pady=10, fill=X)

generate_password_button = Button(right_frame, text="Quit", font=('Helvetica', 16),
                                  bg='#e91d42', fg='white', command=win.quit)
generate_password_button.pack(pady=8, fill=X)

win.mainloop()
