from re import split
from tika import parser
from tkinter import filedialog, mainloop
from tkinter import *

base_notation = 'none'

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
    retour_ligne = 0
    for i in liste_note:
        total += float(i)
    notes = str()
    for i in liste_note:
        retour_ligne += len(i)
        if retour_ligne > 40:
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
    global folder_path
    global filename
    filename = filedialog.askopenfilename()
    folder_path.set(filename)

def process():
    global filename
    global base_notation
    #pdf sequencage
    raw = parser.from_file(filename)
    content_pdf = raw['content']
    text_of_pdf = split('\n',content_pdf)
    text_brut = str()
    for i in text_of_pdf:
        if len(i) >= 10 and len(i) <= 14:
            text_brut += i+' '
    liste = text_brut.split()
    if base_notation == 'cancel':
        print("You decide to cancel the program")
        exit()
    elif base_notation == 'none':
        result.set(('La moyenne des valeurs prisent en compte est de '+str(liste_moyenne(liste))))
    else:
        print('\n\nLa moyenne des valeurs prisent en compte est de',liste_moyenne(liste),'sur',base_notation)
    print('\nEND OF PROGRAM\n')
    

#inititalisation objet parent

root = Tk()
root.title('Projet File analyser - Aymeric GOUDOUT')

#variable servant d'interface utilisateur><machine

folder_path = StringVar()
liste_des_notes = StringVar()
result = StringVar()

#initialisation objets

lbl_result = Label(root, textvariable= result)
lbl_detail = Label(root, textvariable= liste_des_notes)
lbl_title = Label(root,text='Selectionner un fichier dont on souhaite analyser les données (only PDF for V1)')
button_quit = Button(root,text='Quit',command= root.quit)
lbl_of_path = Label(root,textvariable= folder_path)
button_select_folder = Button(root,text="Browse", command=browse_button)
button_process = Button(root,text='Process',command=process)

#placement des objets dans la racine
lbl_title.grid(row=0,column=0,columnspan=3)
button_quit.grid(row=1,column=0)
button_select_folder.grid(row=1, column=2)
lbl_of_path.grid(row=1, column=1)
button_process.grid(row=2,column=1)
lbl_detail.grid(row=3,column=0,columnspan=3)
lbl_result.grid(row=4,column=0,columnspan=3)
mainloop()