from tkinter import*
import tkinter
#webb lien
import webbrowser
def about():

    webbrowser.open_new("https://1drv.ms/w/s!AgV-GZwkjb7Zg7g_tkHUvR1WNL1-xg?e=6FDlUm")

#creer une nouvelle fenetre
fenetre = tkinter.Tk()
#personnnaliser ma fenetre
fenetre.title("Caryophie")
# widgets
mainmenu = tkinter.Menu(fenetre)

first_menu = tkinter.Menu(mainmenu, tearoff=0)
first_menu.add_command(label="Notice")
first_menu.add_command(label="Outils")
first_menu.add_command(label="Autres éléments")

second_menu = tkinter.Menu(mainmenu, tearoff=0)
second_menu.add_command(label="Command1")
second_menu.add_command(label="Command2")
second_menu.add_command(label="À propos", command=about)

mainmenu.add_cascade(label="Menu", menu = first_menu)
mainmenu.add_cascade(label="Aide", menu = second_menu)
import time
def clock():
    t=time.strftime('%I:%M:%S',time.localtime())
    if t!='':
        label1.config(text=t,font='times 25')
    fenetre.after(100,clock)
label1=Label(fenetre,justify='center')
label1.pack(side= TOP)
clock()

fenetre.config(menu=mainmenu)
fenetre.geometry("1200x800")
fenetre.minsize(460, 300)
fenetre.config(background='#F8D583')
#frame
frame = Frame(fenetre, width=310, height=200, bg='#F8D583')

label_title = Label(fenetre, text="Bienvenue dans votre nouvelle aventure",font=("courrier", 22))
label_title.pack()


def fen():
    fen = tkinter.Toplevel(fenetre)
    fen.title("Informations")
    fen.geometry("1200x800")
    fen.config(background='#F8D583')

    def chap():
        text = Text(fen).pack(padx=20, pady=20)
        Button(fen, text='Sauvegarder', width=10, ).pack()
        Button(fen, text='Quitter', width=10, command=fen.quit).pack()

    create = Button(fen, text='création de page', width=40, height=4, command=chap).pack(pady=50, padx=50, expand=YES)

def action():
    Frame2 = Frame(fenetre)
    Frame2.place(relx=0.026, rely=0.063, relheight=0.6, relwidth=0.95)
    Frame2.configure(relief='groove')
    Frame2.configure(borderwidth="2")
    Frame2.configure(background="#ffffff")

    ButtonN1 = Button(Frame2,font=("courrier", 22), command=ajouter_outils)
    ButtonN1.place(relx=0.026, rely=0.163)
    ButtonN1.pack(expand="yes")
    ButtonN1.config(text='''Création d'outils''')

    ButtonN5 = Button(Frame2, font=("courrier", 22), command=ajouter_monstre)
    ButtonN5.place(relx=0.026, rely=0.163)
    ButtonN5.pack(expand="yes")
    ButtonN5.config(text='''Création de monstre''')

    ButtonN2 = Button(Frame2, font=("courrier", 22), command= action_bouton )
    ButtonN2.place(relx=0.026, rely=0.263)
    ButtonN2.pack(expand="yes")
    ButtonN2.config(text='''Création de héros ''')

    ButtonN3 = Button(Frame2, font=("courrier", 22),command= fen)
    ButtonN3.place(relx=0.026, rely=0.363)
    ButtonN3.pack(expand="yes")
    ButtonN3.config(text='''Page édition de texte ''')

    ButtonN4 = Button(Frame2, font=("courrier", 22))
    ButtonN4.place(relx=0.026, rely=0.463)
    ButtonN4.pack(expand="yes")
    ButtonN4.config(text='''Suivant ''')

    Frame2.pack_forget()

    Jouer_button.destroy()
    Editer_button.destroy()

def action_bouton():
    # frame 2

    Frame1 = Frame(fenetre)
    Frame1.place(relx=0.026, rely=0.063, relheight=0.6, relwidth=0.95)
    Frame1.configure(relief='groove')
    Frame1.configure(borderwidth="2")
    Frame1.configure(background="#ffffff")



    labelframe1 = LabelFrame(Frame1, text="Puissance")
    labelframe1.pack(fill="both", expand="yes")
    labelframe1.place(relx=0.042, rely=0.092, relheight=0.241, relwidth=0.448)

    def select(event):
        s = int(scale1.get()+scale2.get()+scale3.get()+scale4.get()+scale5.get())
        print(s)
        if s > 250:
            Button3.config(state=DISABLED)
        else:
            Button3.config(state=NORMAL)

    #widget scale
    v = IntVar

    Framess = Frame(fenetre)
    Framess.place(relx=0.425, rely=0.700, relheight=0.15, relwidth=0.15)
    Framess.configure(relief='groove')
    Framess.configure(borderwidth="2")
    Framess.configure(background="#ffffff")
    label_text = Label(Framess, text="La Valeur doit être <= 250 !")
    label_text.pack()

    scale1 = Scale(labelframe1, variable = v ,from_=0.0, to=100.0, orient= HORIZONTAL, len=400, resolution=1)
    scale1.bind("<B1-Motion>", select)
    scale1.pack()


    labelframe2 = LabelFrame(Frame1, text="habileté")
    labelframe2.pack(fill="both", expand="yes")
    labelframe2.place(relx=0.042, rely=0.345, relheight=0.264, relwidth=0.448)


    scale2 = Scale(labelframe2, variable=v, from_=0.0, to=100.0, orient=HORIZONTAL, len=400, resolution=1)
    scale2.bind("<B1-Motion>", select)
    scale2.pack()

    labelframe3 = LabelFrame(Frame1, text="Chance")
    labelframe3.pack(fill="both", expand="yes")
    labelframe3.place(relx=0.042, rely=0.621, relheight=0.264
                       , relwidth=0.448)

    scale3 = Scale(labelframe3, variable=v, from_=0.0, to=100.0, orient=HORIZONTAL, len=400, resolution=1)
    scale3.bind("<B1-Motion>", select)
    scale3.pack()

    labelframe4 = LabelFrame(Frame1, text="Ruse")
    labelframe4.pack(fill="both", expand="yes")
    labelframe4.place(relx=0.517, rely=0.092, relheight=0.241
                       , relwidth=0.448)

    scale4 = Scale(labelframe4, variable=v, from_=0.0, to=100.0, orient=HORIZONTAL, len=400, resolution=1)
    scale4.bind("<B1-Motion>", select)
    scale4.pack()

    labelframe5 = LabelFrame(Frame1, text="Barre d'appréciation")
    labelframe5.pack(fill="both", expand="yes")
    labelframe5.place(relx=0.517, rely=0.345, relheight=0.264, relwidth=0.448)

    scale5 = Scale(labelframe5, variable=v, from_=0.0, to=100.0, orient=HORIZONTAL, len=400, resolution=1)
    scale5.bind("<B1-Motion>", select)
    scale5.pack()
    # bouton suivant

    Button3 = Button(Frame1)

    Button3.place(relx=0.517, rely=0.621, height=122, width=492)
    Button3.configure(pady=5,padx=5)
    Button3.configure(text='''Suivant''')

def ajouter_outils():
    page = tkinter.Toplevel(fenetre)
    page.geometry('800x700')
    page.config(background='#F8D583')

    afficher_outil_add = ''
    liste_outils = []
    list_outil_tempo = []

    def ajouter_outil_list():
        a = nom_outilString.get()
        list_outil_tempo.append(a)

        b = degat_outilInt.get()
        list_outil_tempo.append(b)

        c = pv_outilInt.get()
        list_outil_tempo.append(c)

        liste_outils.append(list_outil_tempo)
        # après avoir tout appris je voudrais afficher le nom, pv et dégât

        labelaffiche = Label(page, text=(a, b, "dégât", c, "PV"), font=("courrier", 22))
        labelaffiche.pack(padx=0, pady=5)

        # efface éléments de la liste pour pouvoir ajouter d'autres outils
        list_outil_tempo.clear()

    # ajouter nom outils
    labelnom_outil = Label(page, text="Nom de l'outil", font=("courrier", 15))
    labelnom_outil.pack(padx=0, pady=0, )
    nom_outilString = StringVar()
    entrynom_outil = Entry(page, width=20, textvariable=nom_outilString, font=("courrier", 22))
    entrynom_outil.pack(padx=0, pady=1)

    # ajouter dégât outils
    labeldegat_outil = Label(page, text="Dégât de l'outil", font=("courrier", 22))
    labeldegat_outil.pack(padx=0, pady=2)
    degat_outilInt = IntVar()
    entrydegat_outil = Entry(page, width=20, textvariable=degat_outilInt, font=("courrier", 22))
    entrydegat_outil.pack(padx=1, pady=2, )

    # ajouter PV outils
    labelpv_outil = Label(page, text="Point de vie de l'outil", font=("courrier", 22))
    labelpv_outil.pack(padx=0, pady=4)
    pv_outilInt = IntVar()
    entrypv_outil = Entry(page, width=20, textvariable=pv_outilInt, font=("courrier", 22))
    entrypv_outil.pack(padx=1, pady=2, )

    button_ajouter_outils = Button(page, text='Ajouter', font=("courrier", 22), command=ajouter_outil_list)
    button_ajouter_outils.pack(padx=3, pady=1, )

    page.mainloop()

def ajouter_monstre():
    page_1 = tkinter.Toplevel(fenetre)
    page_1.geometry('800x700')
    page_1.config(background='#F8D583')

    afficher_monstre_add = ''
    liste_monstre = []
    list_monstre_tempo = []

    def ajouter_monstre_list():
        a = nom_monstreString.get()
        list_monstre_tempo.append(a)

        b = degat_monstreInt.get()
        list_monstre_tempo.append(b)

        c = pv_monstreInt.get()
        list_monstre_tempo.append(c)

        liste_monstre.append(list_monstre_tempo)
        # après avoir tout appris je voudrais afficher le nom, pv et dégât

        labelaffiche = Label(page_1, text=(a, b, "dégât", c, "PV"), font=("courrier", 22))
        labelaffiche.pack(padx=0, pady=5)

        # efface éléments de la liste pour pouvoir ajouter d'autres outils
        list_monstre_tempo.clear()

    # ajouter nom outils
    labelnom_monstre = Label(page_1, text="Nom du monstre", font=("courrier", 22))
    labelnom_monstre.pack(padx=0, pady=5)
    nom_monstreString = StringVar()
    entrynom_monstre = Entry(page_1, width=20, textvariable=nom_monstreString, font=("courrier", 22))
    entrynom_monstre.pack(padx=1, pady=5)

    # ajouter dégât outils
    labeldegat_monstre = Label(page_1, text="Dégât du monstre", font=("courrier", 22))
    labeldegat_monstre.pack(padx=0, pady=6)
    degat_monstreInt = IntVar()
    entrydegat_monstre = Entry(page_1, width=20, textvariable=degat_monstreInt, font=("courrier", 22))
    entrydegat_monstre.pack(padx=1, pady=6)

    # ajouter PV outils
    labelpv_monstre = Label(page_1, text="Point de vie du monstre", font=("courrier", 22))
    labelpv_monstre.pack(padx=0, pady=9)
    pv_monstreInt = IntVar()
    entrypv_monstre = Entry(page_1, width=20, textvariable=pv_monstreInt, font=("courrier", 22))
    entrypv_monstre.pack(padx=1, pady=9)

    button_ajouter_outils = Button(page_1, text='Ajouter', font=("courrier", 22), command=ajouter_monstre_list)
    button_ajouter_outils.pack(padx=3, pady=1, )

    page_1.mainloop()
def choix():

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
Button(text='quitter',font=("courrier", 18), command=callback).pack(side=BOTTOM)


#ajouter un premier boutton

Jouer_button = Button(frame, text="Jouer au jeu ", font=("courrier", 30), bg='black', fg='white', command=choix,)
Jouer_button.pack(side=LEFT)




#ajouter un deuxième boutton
Editer_button = Button(frame, text="Éditer ", font=("courrier", 30), bg='black', fg='white', command=action,)
Editer_button.pack(side=BOTTOM)

#ajouter
frame.pack(expand=YES)

#afficher
fenetre.mainloop()