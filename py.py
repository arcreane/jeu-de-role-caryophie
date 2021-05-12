from tkinter import*
import tkinter
#webb lien
import webbrowser
def about():
    about_window = tkinter.Toplevel(fenetre)
    about_window.title("Informations")
    about_window.geometry("1200x800")
    about_window.config(background='#F8D583')
    webbrowser.open_new("https://www.youtube.com/watch?v=N4M4W7JPOL4&t=1225s")



#creer une nouvelle fenetre
fenetre = tkinter.Tk()
#personnnaliser ma fenetre
fenetre.title("Caryophie")
# widgets
mainmenu = tkinter.Menu(fenetre)

first_menu = tkinter.Menu(mainmenu, tearoff=0)
first_menu.add_command(label="Notice")
first_menu.add_command(label="outils")
first_menu.add_command(label="autres éléments")

second_menu = tkinter.Menu(mainmenu, tearoff=0)
second_menu.add_command(label="command1")
second_menu.add_command(label="command2")
second_menu.add_command(label="A propos", command=about)

mainmenu.add_cascade(label="Menu", menu = first_menu)
mainmenu.add_cascade(label="Aide", menu = second_menu)

fenetre.config(menu=mainmenu)
fenetre.geometry("1200x800")
fenetre.minsize(460, 300)
fenetre.config(background='#F8D583')
#frame
frame = Frame(fenetre, width=310, height=200, bg='#F8D583')

label_title = Label(fenetre, text="Bienvenue dans votre nouvelle aventure")
label_title.pack()


def fen():
    fen = tkinter.Toplevel(fenetre)
    fen.title("Informations")
    fen.geometry("1200x800")
    fen.config(background='#F8D583')
    text = Text(fen).pack(padx=2, pady=2)
    Button(fen, text='Sauvegarder', width=10, ).pack()
    Button(fen, text='Quitter', width=10, ).pack()






def action_bouton():

    # barre de défilement
    scroll_bar = Scrollbar(fenetre)
    list = Listbox(fenetre, font=('courrier', 9), yscrollcommand=scroll_bar.set)

    for line in range(1, 26):
        list.insert(END, "chapitre" + str(line), )
        scroll_bar.pack(side=LEFT, fill=Y)


    list.pack(side=LEFT, fill=BOTH)
    scroll_bar.config(command=list.yview)


    # frame 2

    Frame1 = Frame(fenetre)
    Frame1.place(relx=0.026, rely=0.063, relheight=0.6, relwidth=0.924)
    Frame1.configure(relief='groove')
    Frame1.configure(borderwidth="2")
    Frame1.configure(background="#ffffff")



    labelframe1 = LabelFrame(Frame1, text="Puissance")
    labelframe1.pack(fill="both", expand="yes")
    labelframe1.place(relx=0.042, rely=0.092, relheight=0.241, relwidth=0.448)

    #widget scale
    v = IntVar
    scale1 = Scale(labelframe1, variable = v ,from_=0.0, to=100.0, orient= HORIZONTAL, len=400, resolution=0.1)
    scale1.pack()


    labelframe2 = LabelFrame(Frame1, text="habileté")
    labelframe2.pack(fill="both", expand="yes")
    labelframe2.place(relx=0.042, rely=0.345, relheight=0.264, relwidth=0.448)


    scale2 = Scale(labelframe2, variable=v, from_=0.0, to=100.0, orient=HORIZONTAL, len=400, resolution=0.1)
    scale2.pack()

    labelframe3 = LabelFrame(Frame1, text="Chance")
    labelframe3.pack(fill="both", expand="yes")
    labelframe3.place(relx=0.042, rely=0.621, relheight=0.264
                       , relwidth=0.448)

    scale3 = Scale(labelframe3, variable=v, from_=0.0, to=100.0, orient=HORIZONTAL, len=400, resolution=0.1)
    scale3.pack()

    labelframe4 = LabelFrame(Frame1, text="Ruse")
    labelframe4.pack(fill="both", expand="yes")
    labelframe4.place(relx=0.517, rely=0.092, relheight=0.241
                       , relwidth=0.448)

    scale4 = Scale(labelframe4, variable=v, from_=0.0, to=100.0, orient=HORIZONTAL, len=400, resolution=0.1)
    scale4.pack()

    labelframe5 = LabelFrame(Frame1, text="Barre d'appréciation")
    labelframe5.pack(fill="both", expand="yes")
    labelframe5.place(relx=0.517, rely=0.345, relheight=0.264, relwidth=0.448)

    scale5 = Scale(labelframe5, variable=v, from_=0.0, to=100.0, orient=HORIZONTAL, len=400, resolution=0.1)
    scale5.pack()
    # bouton suivant

    Button3 = Button(Frame1,command= fen)

    Button3.place(relx=0.517, rely=0.621, height=122, width=492)
    Button3.configure(pady=5,padx=5)
    Button3.configure(text='''Suivant''')




    Jouer_button.destroy()
    Editer_button.destroy()




def choix():

    Button(fenetre, text='choix 1', width=20, height=5).pack(padx=5, pady=5, side=LEFT, expand=TRUE)
    Button(fenetre, text='choix 2', width=20, height=5, ).pack(padx=5, pady=5, side=LEFT, expand=TRUE)
    Button(fenetre, text='choix 3', width=20, height=5, ).pack(padx=5, pady=5, side=LEFT, expand=TRUE)
    Button(fenetre, text='choix 4', width=20, height=5, ).pack(padx=5, pady=5, side=LEFT, expand=TRUE)
    # frame choice
    frame = Frame(fenetre)
    frame.place(relx=0.026, rely=0.063, relheight=0.6, relwidth=0.924)
    frame.configure(relief='groove')
    frame.configure(borderwidth="2")
    frame.configure(background="#ffffff")
    Editer_button.destroy()
    Jouer_button.destroy()


#petit message
from tkinter.messagebox import *
def callback():
    if askyesno('Titre 1', 'Êtes-vous sûr de vouloir quitter?'):
        showwarning('Titre 2', 'Tant pis...')
        command=fenetre.quit()
    else:
        showinfo('Titre 3', 'Vous avez peur!')
        showerror("Titre 4", "Aha")
Button(text='quitter', command=callback).pack()


#ajouter un premier boutton

Jouer_button = Button(frame, text="Jouer au jeu ", font=("courrier", 25), bg='black', fg='white', command=choix,)
Jouer_button.pack(side = LEFT)




#ajouter un deuxième boutton
Editer_button = Button(frame, text="editer ", font=("courrier", 25), bg='black', fg='white',command= action_bouton,)
Editer_button.pack(side= BOTTOM )

#ajouter
frame.pack(expand=YES)

#afficher
fenetre.mainloop()
