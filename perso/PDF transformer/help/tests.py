from re import split
from tika import parser
from tkinter import filedialog
from tkinter import *

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

select_input = input('Vous voulez un scan de quelles données ?\n**(precise if you need a path or not with yes or no)**\n')
base_notation = input('Quelle est la base de notation utilisée ?\n**(you can use none or any integer value)**\n')