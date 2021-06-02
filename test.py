from tkinter import*
import tkinter
import webbrowser
import tkinter.filedialog as tkfd

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

mainmenu.add_cascade(label="Menu", menu=first_menu)
mainmenu.add_cascade(label="Aide", menu=second_menu)

import time
def clock():
    t=time.strftime('%I:%M:%S',time.localtime())
    if t!='':
        label1.config(text=t,font='times 25')
    fenetre.after(100,clock)
label1=Label(fenetre,justify='center')
label1.pack(side=TOP)
clock()

fenetre.config(menu=mainmenu)
fenetre.geometry("1200x800")
fenetre.minsize(460, 300)
fenetre.config(background='#5392f5')
#frame
frame = Frame(fenetre, width=310, height=200, bg='#5392f5')
label_title = Label(fenetre, text="Bienvenue dans votre nouvelle aventure", font=("courrier", 22))
label_title.pack()


def fen():
    fen = tkinter.Toplevel(fenetre)
    fen.title("Informations")
    fen.geometry("1200x800")
    fen.config(background='#5392f5')

    def chap():
        text = Text(fen).pack(padx=20, pady=20)
        Button(fen, text='Sauvegarder', width=10,).pack()
        Button(fen, text='Quitter', width=10, command=fen.destroy).pack()


    create = Button(fen, text='création de page', font=("Bahnschrift", 20), bg='#093a87', fg='white', width=40, height=4, command=chap).pack(pady=50, padx=50, expand=YES)

def action():
    Frame2 = Frame(fenetre)
    Frame2.place(relx=0.026, rely=0.063, relheight=0.8, relwidth=0.95)
    Frame2.configure(relief='groove', borderwidth="2", background="#9cc2ff")

    ButtonN1 = Button(Frame2, text='''Création d'outils''', font=("Bahnschrift", 22), bg='#093a87', fg='white', command=ajouter_outils)
    ButtonN1.pack(expand="yes")

    ButtonN5 = Button(Frame2, text='''Création de monstre''', font=("Bahnschrift", 22), bg='#093a87', fg='white', command=ajouter_monstre)
    ButtonN5.pack(expand="yes")

    ButtonN2 = Button(Frame2, text='''Création de héros ''', font=("Bahnschrift", 22), bg='#093a87', fg='white', command=action_bouton)
    ButtonN2.pack(expand="yes")

    ButtonN3 = Button(Frame2, text='''Page édition de texte ''', font=("Bahnschrift", 22), bg='#093a87', fg='white', command=fen)
    ButtonN3.pack(expand="yes")

    ButtonN6 = Button(Frame2, text='''Ajouter un fond et une musique''', font=("Bahnschrift", 22), bg='#093a87', fg='white', command=ajouter_fondmusique)
    ButtonN6.pack(expand="yes")

    ButtonN4 = Button(Frame2, text='''Suivant ''', font=("Bahnschrift", 22), bg='#09234d', fg='white', command=suivant)
    ButtonN4.place(relx=0.872, rely=0.870)

    ButtonN5 = Button(Frame2, text='''comeback''', font=("Bahnschrift", 22), bg='#09234d', fg='white', command=Frame2.destroy)
    ButtonN5.place(relx=0.015, rely=0.870)

    label_title.destroy()
    Frame2.pack_forget()

def suivant():
    Frame3 =Frame(fenetre)
    Frame3.place(relx=0.026, rely=0.063, relheight=0.8, relwidth=0.95)
    Frame3.configure(relief='groove', borderwidth="2", background="#9cc2ff")

    bouton1 = Button(Frame3, text='''Creer un nouvel environnement''', font=("Bahnschrift", 30), bg='#093a87', fg='white')
    bouton1.pack(expand="yes")

    bouton2 = Button(Frame3, text='''Jouer à mon jeu''', font=("Bahnschrift", 30), bg='#093a87', fg='white')
    bouton2.pack(expand="yes")

    bouton3 = Button(Frame3, text='''Voir mes environnement déjà crées''', font=("Bahnschrift", 30), bg='#093a87', fg='white')
    bouton3.pack(expand="yes")

def action_bouton():
    # frame 2
    Frame1 = Frame(fenetre)
    Frame1.place(relx=0.026, rely=0.063, relheight=0.8, relwidth=0.95)
    Frame1.configure(relief='groove', borderwidth="2", background="#9cc2ff")

    labelframe1 = LabelFrame(Frame1, text="Puissance")
    labelframe1.pack(fill="both", expand="yes")
    labelframe1.place(relx=0.042, rely=0.092, relheight=0.241, relwidth=0.448)

    def select(event):
        s = int(scale1.get() + scale2.get() + scale3.get() + scale4.get() + scale5.get())
        label_text.config(text=s, font='times 25')
        if s > 250:
            Button3.config(state=DISABLED)
        else:
            Button3.config(state=NORMAL)

    #widget scale
    v = IntVar

    Framess = Frame(Frame1)
    Framess.place(relx=0.425, rely=0.9, relheight=0.05, relwidth=0.15)
    Framess.configure(relief='groove', borderwidth="2", background="#ffffff")
    label_text = Label(Framess, text="La Valeur doit être <= 250 !")
    label_text.pack()

    scale1 = Scale(labelframe1, variable=v, from_=0.0, to=100.0, orient=HORIZONTAL, len=400, resolution=1)
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
    labelframe3.place(relx=0.042, rely=0.621, relheight=0.264, relwidth=0.448)

    scale3 = Scale(labelframe3, variable=v, from_=0.0, to=100.0, orient=HORIZONTAL, len=400, resolution=1)
    scale3.bind("<B1-Motion>", select)
    scale3.pack()

    labelframe4 = LabelFrame(Frame1, text="Ruse")
    labelframe4.pack(fill="both", expand="yes")
    labelframe4.place(relx=0.517, rely=0.092, relheight=0.241, relwidth=0.448)

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

    Button3 = Button(Frame1, text='''Suivant''', command=Frame1.destroy)
    Button3.place(relx=0.517, rely=0.621, relheight=0.264, relwidth=0.448)
    Button3.config(pady=5, padx=5)

    #comeback
    ButtonN5 = Button(Frame1, text='''comeback''', font=("courrier", 15), command=Frame1.destroy)
    ButtonN5.pack()


def ajouter_fondmusique():
    page2 = tkinter.Toplevel(fenetre)
    page2.geometry('800x700')
    page2.config(background='#5392f5')

    Button_fond = Button(page2, text='''Fond''', font=("Bahnschrift", 30), bg='#093a87', fg='white', command=fond)
    Button_fond.pack(expand="yes")

    Button_musique = Button(page2, text='''Musique''', font=("Bahnschrift", 30), bg='#093a87', fg='white')
    Button_musique.pack(expand="yes")

    ButtonN5 = Button(page2, text='''comeback''', font=("Bahnschrift", 22), bg='#09234d', fg='white', command=page2.destroy)
    ButtonN5.pack(expand="yes")

def fond():
    path = tkfd.askopenfilename(initialdir="/", title="Select file",
                                    filetypes=(("jpeg files", ".jpg"), ("all files", ".*")))

import csv




def ajouter_outils():
    page = tkinter.Toplevel(fenetre)
    page.geometry('800x700')
    page.config(background='#5392f5')

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


        with open('outils.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(liste_outils)

        # efface éléments de la liste pour pouvoir ajouter d'autres outils
        list_outil_tempo.clear()


    # ajouter nom outils
    labelnom_outil = Label(page, text="Nom de l'outil", font=("courrier", 22))
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

    ButtonN5 = Button(page, text='''comeback''', font=("courrier", 22), command=page.destroy)
    ButtonN5.pack(expand="yes")

    page.mainloop()

def ajouter_monstre():
    page_1 = tkinter.Toplevel(fenetre)
    page_1.geometry('800x700')
    page_1.config(background='#5392f5')

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

    ButtonN5 = Button(page_1, text='''comeback''', font=("courrier", 22), command=page_1.destroy)
    ButtonN5.pack(expand="yes")

    page_1.mainloop()

def choix():

    # frame choice
    frame = Frame(fenetre)
    frame.place(relx=0.026, rely=0.063, relheight=0.8, relwidth=0.924)
    frame.configure(relief='groove', borderwidth="2", background="#9cc2ff")

    Choice = Button(frame, text='''Choisir mon héro''', font=("Bahnschrift", 30), bg='#09234d', fg='white')
    Choice.place(relx=0.350, rely=0.400)

    ButtonN5 = Button(frame, text='''comeback''', font=("Bahnschrift", 15), bg='black', fg='white', command=frame.destroy)
    ButtonN5.place(relx=0.455, rely=0.900)

    label_title.destroy()


#petit message
from tkinter.messagebox import *
def callback():
    if askyesno('Titre 1', 'Êtes-vous sûr de vouloir quitter?'):
        showwarning('Titre 2', 'Tant pis...')
        command=fenetre.quit()
    else:
        showinfo('Titre 3', 'Vous avez peur!')
        showerror("Titre 4", "Aha")
Button(text='quitter',font=("Bahnschrift", 20), bg='black', fg='white', command=callback).pack(side=BOTTOM)


#ajouter un premier boutton

Jouer_button = Button(frame, text="Jouer au jeu ", font=("Elephant", 30), bg='#093a87', fg='white', command=choix)
Jouer_button.place(relx=0.076, rely=0.123)

#ajouter un deuxième boutton
Editer_button = Button(frame, text="Éditer ", font=("Elephant", 30), bg='#093a87', fg='white', command=action)
Editer_button.place(relx=0.250, rely=0.623)

#ajouter
frame.pack(expand=YES)

#afficher
fenetre.mainloop()