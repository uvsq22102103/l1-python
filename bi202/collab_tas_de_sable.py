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
GRILLE = 30
ESPACEMENT = HAUTEUR / GRILLE

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
    global liste_canvas
    liste_canvas = canvas.create_oval(x-rayon,y-rayon,x+rayon,y+rayon,fill=couleur)

def generation():
    canvas.delete('all')
    global config_courante
    config_courante = []
    for i in range(GRILLE):
        config_courante.append([])
        for j in range(GRILLE):
            config_courante[i].append(rd.randint(0,9))
    for x in range(GRILLE):
        for y in range(GRILLE):
            if config_courante[x][y] < 4:
                oval_canvas(ESPACEMENT / 2 + x * ESPACEMENT, ESPACEMENT / 2 + y*ESPACEMENT)
            else:
                oval_canvas(ESPACEMENT / 2 + x * ESPACEMENT, ESPACEMENT / 2 + y*ESPACEMENT,couleur='red')

def actualisation():
    #Permet de mettre à jour l'affichage des grains de sable.
    canvas.delete('all')
    global config_courante
    for x in range(GRILLE):
        for y in range(GRILLE):
            if config_courante[x][y] < 4:
                oval_canvas(ESPACEMENT / 2 + x * ESPACEMENT, ESPACEMENT / 2 + y*ESPACEMENT)
            else:
                oval_canvas(ESPACEMENT / 2 + x * ESPACEMENT, ESPACEMENT / 2 + y*ESPACEMENT,couleur='red')

def cycle():
    global config_courante,old_config
    #Un calcul sur la matrice qui suis le raisonnement d'un tas de sable.
    old_config = config_courante
    for x in range(GRILLE):
        for y in range(GRILLE):
            if old_config[x][y] > 3:
                if (x == 0 or x == GRILLE-1) and (y == 0 or y == GRILLE-1):
                    #Voisinage à deux cases
                    if x == 0 and y == 0:
                        config_courante[x][y]-= 2
                        config_courante[x+1][y]+= 1
                        config_courante[x][y+1]+= 1
                    elif x == GRILLE-1 and y == 0:
                        config_courante[x][y]-= 2
                        config_courante[x-1][y]+= 1
                        config_courante[x][y+1]+= 1
                    elif x == GRILLE-1 and y == GRILLE-1:
                        config_courante[x][y]-= 2
                        config_courante[x-1][y]+= 1
                        config_courante[x][y-1]+= 1
                    else:
                        config_courante[x][y]-= 2
                        config_courante[x+1][y]+= 1
                        config_courante[x][y-1]+= 1
                elif x == 0 or x == GRILLE-1:
                    #Voisinage à trois cases
                    if x == 0 :
                        config_courante[x][y]-= 3
                        config_courante[x+1][y]+= 1
                        config_courante[x][y+1]+= 1
                        config_courante[x][y-1]+= 1
                    else:
                        config_courante[x][y]-= 3
                        config_courante[x-1][y]+= 1
                        config_courante[x][y+1]+= 1
                        config_courante[x][y-1]+= 1
                elif y == 0 or y == GRILLE-1:
                    #Voisinage à trois cases
                    if y == 0:
                        config_courante[x][y]-= 3
                        config_courante[x+1][y]+= 1
                        config_courante[x][y+1]+= 1
                        config_courante[x-1][y]+= 1
                    else:
                        config_courante[x][y]-= 3
                        config_courante[x+1][y]+= 1
                        config_courante[x-1][y]+= 1
                        config_courante[x][y-1]+= 1
                else:
                    #Voisinage complet
                    config_courante[x][y]-= 4
                    config_courante[x][y+1]+= 1
                    config_courante[x][y-1]+= 1
                    config_courante[x+1][y]+= 1
                    config_courante[x-1][y]+= 1

def avalanche():
    for i in range(10):
        cycle()
        actualisation()

def affichage_valeurs():
    global config_courante
    for x in range(GRILLE):
        for y in range(GRILLE):
            canvas.create_text(ESPACEMENT / 2 + x * ESPACEMENT, ESPACEMENT / 2 + y*ESPACEMENT ,fill='white',text=config_courante[x][y])
            

####################
#Programme principal
####################

root = tk.Tk()
root.title('Tas de Sable - Groupe 1')
canvas = tk.Canvas(root,height=HAUTEUR,width=LARGEUR,bg='black')
button_generation = tk.Button(root,text='Génération',command=generation,activebackground='red')
button_avalanche = tk.Button(root,text='Avalanche',command=avalanche)
button_affichage_valeurs = tk.Button(root,text='Valeurs',command=affichage_valeurs)
button_test = tk.Button(root,text='Test',command=cycle)

button_generation.grid(row=0,column=0)
button_avalanche.grid(row=1,column=0)
button_affichage_valeurs.grid(row=2,column=0)
button_test.grid(row=3,column=0)
canvas.grid(row=0,rowspan=4,column=1)

root.mainloop()