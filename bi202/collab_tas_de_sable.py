#############################################
# groupe 1
# Ilerioluwa OLAYODE
# Aymeric GOUDOUT
# Sam BARBOSA
# https://github.com/ilrx/Projet_tas_de_sable
#############################################

######################
#Import des librairies
######################

import tkinter as tk
import random as rd
import time

##########################
#Définition des constantes
##########################

HAUTEUR = 800
LARGEUR = 800
GRILLE = 20

##################################
#Définition des variables globales
##################################

liste_canvas = []
config_courante = []
old_config = []

#########################
#Définition des fonctions
#########################

def oval_canvas(x,y,rayon=7,couleur='blue'):
    liste_canvas = canvas.create_oval(x-rayon,y-rayon,x+rayon,y+rayon,fill=couleur)

def generation():
    canvas.delete('all')
    global config_courante
    config_courante = []
    for i in range(GRILLE):
        config_courante.append([])
        for j in range(GRILLE):
            config_courante[i].append(rd.randint(0,9))
    espacement = HAUTEUR / GRILLE
    for x in range(GRILLE):
        for y in range(GRILLE):
            if config_courante[x][y] < 4:
                oval_canvas(espacement / 2 + x * espacement, espacement / 2 + y*espacement)
            else:
                oval_canvas(espacement / 2 + x * espacement, espacement / 2 + y*espacement,couleur='red')

def avalanche():
    #Cycle + actualisation while Cycle est effectif. 
    pass

def actualisation():
    global config_courante
    #Permet de mettre à jour l'affichage des grains de sable.
    pass

def cycle():
    global config_courante,old_config
    #Un calcul sur la matrice qui suis le raisonnement d'un tas de sable.
    old_config = config_courante

    pass

def affichage_valeurs():
    global config_courante
    espacement = HAUTEUR / GRILLE
    for x in range(GRILLE):
        for y in range(GRILLE):
            canvas.create_text(espacement / 2 + x * espacement, espacement / 2 + y*espacement,fill='white',text=config_courante[x][y])
            

####################
#Programme principal
####################

root = tk.Tk()
root.title('Tas de Sable - Groupe 1')
canvas = tk.Canvas(root,height=HAUTEUR,width=LARGEUR,bg='black')
button_generation = tk.Button(root,text='Génération',command=generation,activebackground='red')
button_avalanche = tk.Button(root,text='Avalanche',command=avalanche)
button_affichage_valeurs = tk.Button(root,text='Valeurs',command=affichage_valeurs)

button_generation.grid(row=0,column=0)
button_avalanche.grid(row=1,column=0)
button_affichage_valeurs.grid(row=2,column=0)
canvas.grid(row=0,rowspan=3,column=1)

root.mainloop()