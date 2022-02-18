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
import copy

##########################
#Définition des constantes
##########################

HAUTEUR = 800
LARGEUR = 800
GRILLE = 5
ESPACEMENT = HAUTEUR / GRILLE
BIG_GRAIN = 10000

##################################
#Définition des variables globales
##################################

liste_canvas = []
config_courante = []
old_config = []
fin_avalanche = False
compteur_cycles = 0

#########################
#Définition des fonctions
#########################

#Création d'un oval symbolisant un grain de sable qui prend pour entrée x et y tel que ce sont les coordonnés de son centre, modulation de la couleur et du rayon du cercle possible.
def oval_canvas(x,y,rayon=7,couleur='blue'):
    global liste_canvas
    liste_canvas.append(canvas.create_oval(x-rayon,y-rayon,x+rayon,y+rayon,fill=couleur,tags="grains"))

#Création d'une liste matrice contenant des valeurs randomisées comprises entre 0 et 9, cette liste est ensuite utilisée comme base pour construire le quadrillage affiché sur la canvas.
def generation(event=0):
    canvas.delete('all')
    global config_courante,old_config,fin_avalanche,compteur_cycles,liste_canvas
    liste_canvas = []
    config_courante = []
    old_config = []
    fin_avalanche = True
    compteur_cycles = 0
    compteur.set(compteur_cycles)
    for i in range(GRILLE):
        config_courante.append([])
        for j in range(GRILLE):
            config_courante[i].append(rd.randint(0,9))
    for x in range(GRILLE):
        for y in range(GRILLE):
            if config_courante[x][y] == 0:
                oval_canvas(ESPACEMENT / 2 + x * ESPACEMENT, ESPACEMENT / 2 + y*ESPACEMENT,couleur='gray',rayon=ESPACEMENT/2)
            elif config_courante[x][y] == 1:
                oval_canvas(ESPACEMENT / 2 + x * ESPACEMENT, ESPACEMENT / 2 + y*ESPACEMENT,couleur='#00ff7f',rayon=ESPACEMENT/2)
            elif config_courante[x][y] == 2:
                oval_canvas(ESPACEMENT / 2 + x * ESPACEMENT, ESPACEMENT / 2 + y*ESPACEMENT,couleur='#79f8f8',rayon=ESPACEMENT/2)
            elif config_courante[x][y] == 3:
                oval_canvas(ESPACEMENT / 2 + x * ESPACEMENT, ESPACEMENT / 2 + y*ESPACEMENT,couleur='#ff5e4d',rayon=ESPACEMENT/2)
            elif config_courante[x][y] == 4:
                oval_canvas(ESPACEMENT / 2 + x * ESPACEMENT, ESPACEMENT / 2 + y*ESPACEMENT,couleur='#c11be7',rayon=ESPACEMENT/2)
            elif config_courante[x][y] == 5:
                oval_canvas(ESPACEMENT / 2 + x * ESPACEMENT, ESPACEMENT / 2 + y*ESPACEMENT,couleur='#318ce7',rayon=ESPACEMENT/2)
            elif config_courante[x][y] == 6:
                oval_canvas(ESPACEMENT / 2 + x * ESPACEMENT, ESPACEMENT / 2 + y*ESPACEMENT,couleur='yellow',rayon=ESPACEMENT/2)
            elif config_courante[x][y] == 7:
                oval_canvas(ESPACEMENT / 2 + x * ESPACEMENT, ESPACEMENT / 2 + y*ESPACEMENT,couleur='#a83c71',rayon=ESPACEMENT/2)
            elif config_courante[x][y] == 8:
                oval_canvas(ESPACEMENT / 2 + x * ESPACEMENT, ESPACEMENT / 2 + y*ESPACEMENT,couleur='#9b1c3e',rayon=ESPACEMENT/2)
            else:
                oval_canvas(ESPACEMENT / 2 + x * ESPACEMENT, ESPACEMENT / 2 + y*ESPACEMENT,couleur='#810a0a',rayon=ESPACEMENT/2)


def blank_pattern(event=0):
    canvas.delete('all')
    global config_courante,old_config,fin_avalanche,compteur_cycles,liste_canvas
    liste_canvas = []
    config_courante = []
    old_config = []
    fin_avalanche = True
    compteur_cycles = 0
    compteur.set(compteur_cycles)
    for x in range(GRILLE):
        config_courante.append([])
        for y in range(GRILLE):
            config_courante[x].append(0)
            oval_canvas(ESPACEMENT / 2 + x * ESPACEMENT, ESPACEMENT / 2 + y*ESPACEMENT,couleur='gray',rayon=ESPACEMENT/2)


def actualisation():
    #Permet de mettre à jour l'affichage des grains de sable.
    canvas.delete('all')
    global config_courante,liste_canvas
    liste_canvas = []
    for x in range(GRILLE):
        for y in range(GRILLE):
            if config_courante[x][y] == 0:
                oval_canvas(ESPACEMENT / 2 + x * ESPACEMENT, ESPACEMENT / 2 + y*ESPACEMENT,couleur='gray',rayon=ESPACEMENT/2)
            elif config_courante[x][y] == 1:
                oval_canvas(ESPACEMENT / 2 + x * ESPACEMENT, ESPACEMENT / 2 + y*ESPACEMENT,couleur='#00ff7f',rayon=ESPACEMENT/2)
            elif config_courante[x][y] == 2:
                oval_canvas(ESPACEMENT / 2 + x * ESPACEMENT, ESPACEMENT / 2 + y*ESPACEMENT,couleur='#79f8f8',rayon=ESPACEMENT/2)
            elif config_courante[x][y] == 3:
                oval_canvas(ESPACEMENT / 2 + x * ESPACEMENT, ESPACEMENT / 2 + y*ESPACEMENT,couleur='#ff5e4d',rayon=ESPACEMENT/2)
            elif config_courante[x][y] == 4:
                oval_canvas(ESPACEMENT / 2 + x * ESPACEMENT, ESPACEMENT / 2 + y*ESPACEMENT,couleur='#c11be7',rayon=ESPACEMENT/2)
            elif config_courante[x][y] == 5:
                oval_canvas(ESPACEMENT / 2 + x * ESPACEMENT, ESPACEMENT / 2 + y*ESPACEMENT,couleur='#318ce7',rayon=ESPACEMENT/2)
            elif config_courante[x][y] == 6:
                oval_canvas(ESPACEMENT / 2 + x * ESPACEMENT, ESPACEMENT / 2 + y*ESPACEMENT,couleur='yellow',rayon=ESPACEMENT/2)
            elif config_courante[x][y] == 7:
                oval_canvas(ESPACEMENT / 2 + x * ESPACEMENT, ESPACEMENT / 2 + y*ESPACEMENT,couleur='#a83c71',rayon=ESPACEMENT/2)
            elif config_courante[x][y] == 8:
                oval_canvas(ESPACEMENT / 2 + x * ESPACEMENT, ESPACEMENT / 2 + y*ESPACEMENT,couleur='#9b1c3e',rayon=ESPACEMENT/2)
            else:
                oval_canvas(ESPACEMENT / 2 + x * ESPACEMENT, ESPACEMENT / 2 + y*ESPACEMENT,couleur='#810a0a',rayon=ESPACEMENT/2)


def cycle():
    global config_courante,old_config
    #Un calcul sur la matrice qui suis le raisonnement d'un tas de sable.
    old_config = copy.deepcopy(config_courante)
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


def avalanche(event=0):
    #boucle temporaire en attendant de trouver un moyen de faire des comparaison avec la matrice -1.
    global config_courante,old_config,fin_avalanche,compteur_cycles
    fin_avalanche = False
    while config_courante != old_config and fin_avalanche is False:
        cycle()
        actualisation()
        compteur.set(compteur_cycles)
        root.update()
        compteur_cycles += 1
        time.sleep(0.1)
    compteur.set(compteur_cycles)


def affichage_valeurs(event=0):
    global config_courante
    for x in range(GRILLE):
        for y in range(GRILLE):
            canvas.create_text(ESPACEMENT / 2 + x * ESPACEMENT, ESPACEMENT / 2 + y*ESPACEMENT ,fill='white',text=config_courante[x][y])          


def fin_aval(event=0):
    global fin_avalanche
    fin_avalanche = True


def infos(event=0):
    informations = tk.Tk()
    informations.title('Infos')
    label_info = tk.Label(informations,text='\nListe des raccourcis :\n\nSpace = Génération\nReturn = Start\nBackSpace = Stop\nE = Génération de pattern vide\nV = Affiche les valeurs du quadrillage\nLeft click = ajout de 1 au grain de sable cliqué\n   Shift-Left click = ajout de 10000 au grain de sable cliqué   \nRight click = on enlève 1 au grain de sable cliqué\n\n')
    label_info.grid(row=0,column=0)
    informations.mainloop()


def on_click(event):
    le_grain = event.widget.find_closest(event.x,event.y)[0]%(GRILLE**2)
    variable_calcul1 = 0
    variable_calcul2 = 0
    if event.widget.find_closest(event.x,event.y)[0] != 0 and le_grain == 0:
        le_grain = GRILLE
        variable_calcul1 = le_grain//GRILLE
        variable_calcul2 = variable_calcul1 * GRILLE
        le_grain = le_grain-variable_calcul2-1
        if le_grain == -1:
            le_grain = GRILLE-1
        res = [le_grain,le_grain]
    else:
        variable_calcul1 = le_grain//GRILLE
        variable_calcul2 = variable_calcul1 * GRILLE
        le_grain = le_grain-variable_calcul2-1
        if le_grain == -1:
            le_grain = GRILLE-1
            variable_calcul1-= 1
        res = [variable_calcul1,le_grain]
    return(res)


def left_click_grain(event):
    coords = on_click(event)
    if config_courante[coords[0]][coords[1]] < 9:
        config_courante[coords[0]][coords[1]] += 1
    actualisation()


def middle_click_grain(event):
    global BIG_GRAIN
    coords = on_click(event)
    config_courante[coords[0]][coords[1]] += BIG_GRAIN
    actualisation()


def right_click_grain(event):
    coords = on_click(event)
    if config_courante[coords[0]][coords[1]] > 0:
        config_courante[coords[0]][coords[1]] -= 1
    actualisation()


####################
#Programme principal
####################

#Création du Widget parent
root = tk.Tk()

#Variable Tkinter
compteur = tk.IntVar()

#Définition des raccourcis
root.bind_all('e',blank_pattern)
root.bind_all('<BackSpace>',fin_aval)
root.bind_all('<Return>',avalanche)
root.bind_all('<space>',generation)
root.bind_all('i',infos)
root.bind_all('v',affichage_valeurs)

#Interface graphique
root.title('Tas de Sable - Groupe 1')
canvas = tk.Canvas(root,height=HAUTEUR,width=LARGEUR,bg='black')
canvas.tag_bind("grains","<ButtonPress-1>",left_click_grain)
canvas.tag_bind("grains","<Shift-ButtonPress-1>",middle_click_grain)
canvas.tag_bind("grains","<ButtonPress-3>",right_click_grain)
blank_pattern()
button_generation = tk.Button(root,text='Génération',command=generation,activebackground='red')
button_avalanche = tk.Button(root,text='Start',command=avalanche)
button_affichage_valeurs = tk.Button(root,text='Valeurs',bg='gray',command=affichage_valeurs)
button_stop = tk.Button(root,text='Stop',command=fin_aval)
label_compteur = tk.Label(root,textvariable=compteur,relief='groove')
button_infos = tk.Button(root,text='Infos',bg='gray',command=infos)
button_generation.grid(row=0,column=0,columnspan=2)
button_avalanche.grid(row=4,column=0)
button_affichage_valeurs.grid(row=4,column=3)
button_stop.grid(row=4,column=1)
label_compteur.grid(row=5,column=0,columnspan=2)
button_infos.grid(row=5,column=3)
canvas.grid(row=0,rowspan=6,column=2)

#################
#Fin du programme
#################

root.mainloop()