#!/usr/bin/env python

# -*- coding: utf-8 -*-

from tkinter import *

def petit_format():
    pass

def normal():
    pass

def grand_format():
    pass

def fond_blanc():
    pass

def fond_sombre():
    pass


# Création de la fenêtre

fen_princ = Tk()

fen_princ.title("Mon application à moi que j'ai")

fen_princ.geometry("900x600")


# Création du cadre-conteneur pour les menus

zoneMenu = Frame(fen_princ, borderwidth=3, bg='#557788')

zoneMenu.pack(fill=X)


# Création de l'onglet Fichier

menuFichier = Menubutton(zoneMenu, text='Fichier', width='20', borderwidth=2, bg='gray', activebackground='darkorange',relief = RAISED)

menuFichier.grid(row=0,column=0)


# Création de l'onglet Edition

menuEdit = Menubutton(zoneMenu, text='Editer', width='20', borderwidth=2, bg='gray', activebackground='darkorange',relief = RAISED)

menuEdit.grid(row=0,column=1)


# Création de l'onglet Format

menuFormat = Menubutton(zoneMenu, text='Format', width='20', borderwidth=2, bg='gray', activebackground='darkorange',relief = RAISED)

menuFormat.grid(row=0,column=2)

#Créa onglet Affichage

menuAffichage = Menubutton(zoneMenu, text='Affichage',width='20',borderwidth=2,bg='gray',activebackground='darkorange',relief= RAISED)

menuAffichage.grid(row=0,column=3)

#Sous onglet

menu_d_affichage = Menu(menuAffichage)
menu_d_affichage.add_command(label='Petit format',command= petit_format)
menu_d_affichage.add_command(label='Normal',command=normal)
menu_d_affichage.add_command(label='Grand format',command=grand_format)
menu_d_affichage.add_command(label='Fond blanc',command=fond_blanc)
menu_d_affichage.add_command(label='Fond sombre',command=fond_sombre)

menuAffichage.configure(menu=menu_d_affichage)

# Lancement de la surveillance sur la fenêtre

fen_princ.mainloop()