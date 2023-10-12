from tkinter import *

win = Tk()
win.geometry('500x500')
win.title('Hmak App with Menu')
win['bg'] = '#a027a7'
win.resizable(height=False, width=False)

my_menu = Menu(win)
# ajouter des sous-onglets
# sous onglets pour fichier
fichier = Menu(my_menu, tearoff=0)
fichier.add_command(label='New project')
fichier.add_command(label='New')
fichier.add_command(label='Open project')
fichier.add_command(label='exit')

# sous onglets pour editeur
Editeur = Menu(my_menu, tearoff=0)
Editeur.add_command(label='Undo')
Editeur.add_command(label='Cut')
Editeur.add_command(label='Copy')
Editeur.add_command(label='Delete')

# sous onglets pour Help
aide = Menu(my_menu, tearoff=0)
aide.add_command(label="app version")
aide.add_command(label="checking for update")

#  principaux onglets du menu
my_menu.add_cascade(label="Fichier", menu=fichier)
my_menu.add_cascade(label='Editeur', menu=Editeur)
my_menu.add_cascade(label='Help', menu=aide)

# afficher le menu
win.config(menu=my_menu)

win.mainloop()
