import os
from re import split
from tika import parser
from tkinter import filedialog, mainloop
from tkinter import *

liste_note = []
base_notation = 'none'
file_suffix = 'none'

def virguleEnPoint(mot):
    if ',' in mot:
        chiffre = mot.replace(',','.')
        return(chiffre)
    else:
        return(mot)

def liste_moyenne(liste):
    #Traitement normé d'une liste et qui prend en compte les valeur < 5 caractères.
    global liste_note
    liste_note = []
    for i in liste:
        if len(i) < 5:
            liste_note.append(virguleEnPoint(i))
    total = 0
    retour_ligne = 0
    for i in liste_note:
        total += float(i)
    notes = str()
    for i in liste_note:
        retour_ligne += len(i)
        if retour_ligne > 55:
            notes += '\n' + i + ' '
            retour_ligne = 0
        else:
            notes += i + ' '
    notes += '\nIl y a '+str(len(liste_note))+' valeurs de prisent en compte.'
    liste_des_notes.set(notes)
    return (round(total/len(liste_note),2))

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path,filename,file_suffix
    filename = filedialog.askopenfilename()
    folder_path.set(filename)
    #identification suffix
    file_path, file_suffix = os.path.splitext(filename)
    file_suffix_state.set('Fichier '+file_suffix+' détecté.')

def note_cc_5():
    global filename,file_suffix
    #Différent traitement des données selon le suffix du fichier
    if file_suffix == 'none':
        liste_des_notes.set('ERREUR')
        result.set('Please select a file by Browse')
    elif file_suffix == '.pdf':
        #pdf sequencage
        raw = parser.from_file(filename)
        content_pdf = raw['content']
        text_of_pdf = split('\n',content_pdf)
        text_brut = str()
        for i in text_of_pdf:
            if len(i) >= 10 and len(i) <= 14:
                text_brut += i+' '
        liste = text_brut.split()
        result.set(('La moyenne de ce CC est de '+str(liste_moyenne(liste))+' /5'))
    else:
        liste_des_notes.set('ERREUR')
        result.set('Fichier '+file_suffix+' non pris en compte.')

def note_cc_20():
    global filename,file_suffix
    #Différent traitement des données selon le suffix du fichier
    if file_suffix == 'none':
        liste_des_notes.set('ERREUR')
        result.set('Please select a file by Browse')
    elif file_suffix == '.pdf':
        #pdf sequencage
        raw = parser.from_file(filename)
        content_pdf = raw['content']
        text_of_pdf = split('\n',content_pdf)
        text_brut = str()
        for i in text_of_pdf:
            if len(i) >= 10 and len(i) <= 14:
                text_brut += i+' '
        liste = text_brut.split()
        result.set(('La moyenne de ce CC est de '+str(liste_moyenne(liste))+' /20'))
    else:
        liste_des_notes.set('ERREUR')
        result.set('Fichier '+file_suffix+' non pris en compte.')

    

#inititalisation objet parent

root = Tk()
root.title('Projet File analyser - Aymeric GOUDOUT')

#variable servant d'interface utilisateur><machine

folder_path = StringVar()
liste_des_notes = StringVar()
result = StringVar()
file_suffix_state = StringVar()

#initialisation objets

lbl_suffix_file = Label(root, textvariable= file_suffix_state)
lbl_result = Label(root, textvariable= result)
lbl_detail = Label(root, textvariable= liste_des_notes)
lbl_title = Label(root,text='Selectionner un fichier dont on souhaite analyser les données (only PDF for v1.1)')
button_quit = Button(root,text='Quit',command= root.quit)
lbl_of_path = Label(root,textvariable= folder_path)
button_select_folder = Button(root,text="Browse", command=browse_button)

#onglet déroulant pdf

button_pdf_process = Menubutton(root,text='PDF Process',activebackground='pink',relief= RAISED)
pdf_process = Menu(button_pdf_process)
pdf_process.add_command(label='CC notes /5',command=note_cc_5)
pdf_process.add_command(label='CC notes /20',command=note_cc_20)

button_pdf_process.configure(menu=pdf_process)

#placement des objets dans la racine
lbl_title.grid(row=0,column=0,columnspan=3)
button_quit.grid(row=1,column=0)
button_select_folder.grid(row=1, column=2)
lbl_of_path.grid(row=1, column=1)
button_pdf_process.grid(row=2,column=1)
lbl_detail.grid(row=3,column=0,columnspan=3)
lbl_result.grid(row=4,column=0,columnspan=3)
lbl_suffix_file.grid(row=5,column=1)
mainloop()