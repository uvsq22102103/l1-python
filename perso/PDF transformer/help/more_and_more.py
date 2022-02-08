import os
from re import split
from tika import parser
from tkinter import filedialog, mainloop
import tkinter as tk

def browse_button():
    # Allow user to select a directory and store it in global var
    filename = filedialog.askopenfilename()
    return(filename)

def virguleEnPoint(mot):
    if ',' in mot:
        chiffre = mot.replace(',','.')
        return(chiffre)
    else:
        return(mot)

def liste_moyenne(liste):
    #Traitement normé d'une liste et qui prend en compte les valeur < 5 caractères.
    liste_note = []
    for i in liste:
        if len(i) < 5:
            liste_note.append(virguleEnPoint(i))
    total = 0
    for i in liste_note:
        total += float(i)
    return (round(total/len(liste_note),2))

select_input = input('Scan de PDF ou copier coller\n**(precise if you need a ask filedir or not with yes or no)**\n')
if select_input == 'yes':
    entree = browse_button()
    #pdf sequencage
    raw = parser.from_file(entree)
    content_pdf = raw['content']
    text_of_pdf = split('\n',content_pdf)
    text_brut = str()
    for i in text_of_pdf:
        if len(i) >= 10 and len(i) <= 14:
            text_brut += i+' '
    liste = text_brut.split()
elif select_input == 'no':
    entree = input('Saisir les données de sujet:\n')
    liste = entree.split()
else:
    print('Entry not correct, please restart the program')
    exit()
base_notation = input('Quelle est la base de notation utilisée ?\n**(you can use cancel, none or any integer value for reference)**\n')
if base_notation == 'cancel':
    print("You decide to cancel the program")
    exit()
elif base_notation == 'none':
    print('La moyenne des valeurs prisent en compte est de',liste_moyenne(liste))
else:
    print('La moyenne des valeurs prisent en compte est de',liste_moyenne(liste),'sur',base_notation)
print('\nEND OF PROGRAM\n')