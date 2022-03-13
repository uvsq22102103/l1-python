#############################################
# groupe 1
# Ilerioluwa OLAYODE
# Aymeric GOUDOUT
# Sam BARBOSA
# https://github.com/ilrx/Projet_tas_de_sable
#############################################

#couleurs utilisées : #ffffff #efe2e2 #e0c6c6 #d1aaaa #c28e8d #b27171 #a35555 #943938 #851d1c #760100

######################
#Import des librairies
######################

import tkinter as tk
from tkinter.filedialog import askopenfilename
import random as rd
import copy
import os

##########################
#Définition des constantes
##########################

HAUTEUR = 800
LARGEUR = 800
BIG_GRAIN = 10000
DIREC = os.path.realpath(__file__)[0:-21]
COULEUR = ['gray','red','blue','purple','yellow']

##################################
#Définition des variables globales
##################################

liste_canvas = []
config_courante = []
old_config = []
fin_avalanche = False
compteur_cycles = 0
scale_variable = 0
grille = 11
compteur_valeurs = 0
espacement = HAUTEUR / grille

#########################
#Définition des fonctions
#########################

def update_color(objet,color):
    canvas.itemconfig(objet,fill=color)


def oval_canvas(x,y,rayon=7,line=int(),couleur='blue'):
    global liste_canvas
    liste_canvas[line].append(canvas.create_rectangle(x-rayon+1,y-rayon+1,x+rayon+1,y+rayon+1,fill=couleur,tags="grains"))


def actualisation_initiale():
    canvas.delete('all')
    global config_courante,liste_canvas
    liste_canvas = []
    for x in range(grille):
        liste_canvas.append([])
        for y in range(grille):
            if config_courante[x][y] == 0:
                oval_canvas(espacement / 2 + x * espacement, espacement / 2 + y*espacement,couleur=COULEUR[0],rayon=espacement/2,line=x)
            elif config_courante[x][y] == 1:
                oval_canvas(espacement / 2 + x * espacement, espacement / 2 + y*espacement,couleur=COULEUR[1],rayon=espacement/2,line=x)
            elif config_courante[x][y] == 2:
                oval_canvas(espacement / 2 + x * espacement, espacement / 2 + y*espacement,couleur=COULEUR[2],rayon=espacement/2,line=x)
            elif config_courante[x][y] == 3:
                oval_canvas(espacement / 2 + x * espacement, espacement / 2 + y*espacement,couleur=COULEUR[3],rayon=espacement/2,line=x)
            else:
                oval_canvas(espacement / 2 + x * espacement, espacement / 2 + y*espacement,couleur=COULEUR[4],rayon=espacement/2,line=x)


def actualisation():
    global config_courante,liste_canvas
    for x in range(grille):
        for y in range(grille):
            if config_courante[x][y] == 0:
                update_color(objet = liste_canvas[x][y], color=COULEUR[0])
            elif config_courante[x][y] == 1:
                update_color(objet = liste_canvas[x][y], color=COULEUR[1])
            elif config_courante[x][y] == 2:
                update_color(objet = liste_canvas[x][y], color=COULEUR[2])
            elif config_courante[x][y] == 3:
                update_color(objet = liste_canvas[x][y], color=COULEUR[3])
            else:
                update_color(objet = liste_canvas[x][y], color=COULEUR[4])


def gen_window(event=0):
    global root_gen,gen_window_grille
    root_gen = tk.Toplevel(root)
    root_gen.title('All the generations')
    button_gen_random = tk.Button(root_gen,text='Random',command=lambda:generations(gen_type='random'))
    button_gen_pile_centree = tk.Button(root_gen,text='Pile centrée',command=lambda:generations(gen_type='pile centrée'))
    button_gen_blank = tk.Button(root_gen,text='Blank',command=generations)
    button_gen_max = tk.Button(root_gen,text='Max stable',command=lambda:generations(gen_type='max stable'))
    button_gen_ecoulement = tk.Button(root_gen,text='Ecoulement',command=lambda:generations(gen_type='ecoulement'))
    button_gen_identity = tk.Button(root_gen,text='Identity',command=lambda:generations(gen_type='identity'))
    entry_gen = tk.Entry(root_gen,textvariable=gen_window_grille)
    button_gen_random.grid()
    button_gen_pile_centree.grid(row=0,column=1)
    button_gen_blank.grid(row=0,column=2)
    button_gen_max.grid(row=1,column=0)
    button_gen_ecoulement.grid(row=1,column=1)
    button_gen_identity.grid(row=1,column=2)
    entry_gen.grid(row=2,column=1)


def generation_initiale(event=0):
    canvas.delete('all')
    global config_courante,old_config,fin_avalanche,compteur_cycles,grille,espacement,gen_window_grille
    grille = gen_window_grille.get()
    espacement = HAUTEUR / grille
    config_courante = []
    old_config = []
    fin_avalanche = True
    compteur_cycles = 0
    compteur.set(compteur_cycles)
    for x in range(grille):
        config_courante.append([])
        for y in range(grille):
            config_courante[x].append(0)
    actualisation_initiale()
    

def generations(gen_type='blank'):
    canvas.delete('all')
    global config_courante,old_config,fin_avalanche,compteur_cycles,root_gen,grille,espacement,gen_window_grille
    grille = gen_window_grille.get()
    espacement = HAUTEUR / grille
    config_courante = []
    old_config = []
    fin_avalanche = True
    compteur_cycles = 0
    compteur.set(compteur_cycles)
    if gen_type == 'random':
        for i in range(grille):
            config_courante.append([])
            for j in range(grille):
                config_courante[i].append(rd.randint(0,3))
    elif gen_type == 'pile centrée':
        for x in range(grille):
            config_courante.append([])
            for y in range(grille):
                config_courante[x].append(0)
        canvas.create_text(HAUTEUR//2,LARGEUR//2,text='Action requise au terminal',fill='white')
        config_courante[grille//2][grille//2] = int(input('Quel est la valeur N à attribuer au grain de sable central ?   '))
    elif gen_type == 'blank':
        for x in range(grille):
            config_courante.append([])
            for y in range(grille):
                config_courante[x].append(0)
    elif gen_type == 'identity':
        for x in range(grille):
            config_courante.append([])
            for y in range(grille):
                config_courante[x].append(6)
    elif gen_type == 'max stable':
        for x in range(grille):
            config_courante.append([])
            for y in range(grille):
                config_courante[x].append(3)
    elif gen_type == 'ecoulement':
        for i in range(grille):
            config_courante.append([])
            for j in range(grille):
                config_courante[i].append(rd.randint(0,5))
    actualisation_initiale()
    root_gen.destroy()
    

def cycle():
    global config_courante,old_config,grille
    #Un calcul sur la matrice qui suis le raisonnement d'un tas de sable.
    old_config = copy.deepcopy(config_courante)
    for x in range(grille):
        for y in range(grille):
            if old_config[x][y] > 3:
                if (x == 0 or x == grille-1) and (y == 0 or y == grille-1):
                    #Voisinage à deux cases
                    if x == 0 and y == 0:
                        config_courante[x][y]-= 4
                        config_courante[x+1][y]+= 1
                        config_courante[x][y+1]+= 1
                    elif x == grille-1 and y == 0:
                        config_courante[x][y]-= 4
                        config_courante[x-1][y]+= 1
                        config_courante[x][y+1]+= 1
                    elif x == grille-1 and y == grille-1:
                        config_courante[x][y]-= 4
                        config_courante[x-1][y]+= 1
                        config_courante[x][y-1]+= 1
                    else:
                        config_courante[x][y]-= 4
                        config_courante[x+1][y]+= 1
                        config_courante[x][y-1]+= 1
                elif x == 0 or x == grille-1:
                    #Voisinage à trois cases
                    if x == 0 :
                        config_courante[x][y]-= 4
                        config_courante[x+1][y]+= 1
                        config_courante[x][y+1]+= 1
                        config_courante[x][y-1]+= 1
                    else:
                        config_courante[x][y]-= 4
                        config_courante[x-1][y]+= 1
                        config_courante[x][y+1]+= 1
                        config_courante[x][y-1]+= 1
                elif y == 0 or y == grille-1:
                    #Voisinage à trois cases
                    if y == 0:
                        config_courante[x][y]-= 4
                        config_courante[x+1][y]+= 1
                        config_courante[x][y+1]+= 1
                        config_courante[x-1][y]+= 1
                    else:
                        config_courante[x][y]-= 4
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
    global config_courante,old_config,fin_avalanche,compteur_cycles
    fin_avalanche = False
    while config_courante != old_config and fin_avalanche is False:
        cycle()
        actualisation()
        compteur.set(compteur_cycles)
        root.update()
        compteur_cycles += 1
    compteur.set(compteur_cycles)


def affichage_valeurs(event=0):
    global compteur_valeurs,config_courante
    compteur_valeurs += 1
    if compteur_valeurs % 2 == 0:
        canvas.delete('values')
    else:
        for x in range(grille):
            for y in range(grille):
                canvas.create_text(espacement / 2 + x * espacement, espacement / 2 + y*espacement ,fill='black',text=config_courante[x][y],tags='values')


def fin_aval(event=0):
    global fin_avalanche
    fin_avalanche = True


def infos(event=0):
    informations = tk.Toplevel(root)
    informations.title('Infos')
    label_info = tk.Label(informations,text='\nListe des raccourcis :\n\nSpace = Génération\nReturn = Start\nBackSpace = Stop\nE = Génération de pattern vide\nV = Affiche les valeurs du quadrillage\nLeft click = ajout de 1 au grain de sable cliqué\n   Shift-Left click = ajout de 10000 au grain de sable cliqué   \nRight click = on enlève 1 au grain de sable cliqué\n\n')
    label_info.grid(row=0,column=0)


def on_click(event):
    global grille,liste_canvas
    id_grain = event.widget.find_closest(event.x,event.y)[0]
    for sublist in range(len(liste_canvas)):
        if id_grain in liste_canvas[sublist]:
            case = [sublist,liste_canvas[sublist].index(id_grain)]
    return(case)


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


def save():
    print('The save will be placed at : ',DIREC)
    confirmation = False
    while not confirmation:
        txt_name = input('Choose the name of your save : ')
        txt_dir = DIREC + txt_name +'.txt'
        print('This is the save path :  ',txt_dir)
        conf = input('Do you agree the proposition ? (yes or no)\n')
        if conf == 'yes' :
            confirmation = True
    sauvegarde = open(txt_dir,'w')
    for i in config_courante:
        line = ';'
        for j in i:
            line += str(j)+';'
        sauvegarde.write(line+'\n')
    sauvegarde.close()
    print('Sauvegarde effectuée !')
    root_save.destroy()


def load(parametre='replace'):
    global config_courante,old_config,grille,espacement
    txt_dir = askopenfilename(initialdir=DIREC)
    print('You select : ',txt_dir)
    sauvegarde = open(txt_dir)
    lines = sauvegarde.readlines()
    if parametre == 'replace':
        grille = len(lines)
        espacement = HAUTEUR / grille
        print('Quadrillage paramétré :',grille)
        config_courante = []
        old_config = []
        for line in lines:
            line = line.replace('\n','')
            line = line.split(';')
            line.remove('')
            line.remove('')
            for character in range(len(line)):
                line[character] = int(line[character])
            config_courante.append(line)
    elif parametre == 'add':
        if grille == len(lines):
            for line in range(grille):
                lines[line] = lines[line].replace('\n','')
                lines[line] = lines[line].split(';')
                lines[line].remove('')
                lines[line].remove('')
                line_config_courante = config_courante[line]
                for number in range(grille):
                    line_config_courante[number] += int(lines[line][number])
                config_courante[line] = copy.deepcopy(line_config_courante)
        else:
            print('Le quadrillage affiché sur le canvas est incompatible avec celui du fichier txt : ',txt_dir)
    elif parametre == 'substract':
        if grille == len(lines):
            for line in range(grille):
                lines[line] = lines[line].replace('\n','')
                lines[line] = lines[line].split(';')
                lines[line].remove('')
                lines[line].remove('')
                line_config_courante = config_courante[line]
                for number in range(grille):
                    line_config_courante[number] -= int(lines[line][number])
                    if line_config_courante[number] < 0:
                        line_config_courante[number] = 0
                config_courante[line] = copy.deepcopy(line_config_courante)
        else:
            print('Le quadrillage affiché sur le canvas est incompatible avec celui du fichier txt : ',txt_dir)
    actualisation_initiale()
    root_save.destroy()


def saves_txt():
    global root_save
    root_save = tk.Toplevel(root)
    button_save = tk.Button(root_save,text='Save',command=save)
    button_load = tk.Button(root_save,text='Load',command=load)
    button_load_add = tk.Button(root_save,text='Load & Add',command=lambda:load(parametre='add'))
    button_load_sub = tk.Button(root_save,text='Load & Soustract',command=lambda:load(parametre='substract'))
    button_save.grid(row=0,column=0)
    button_load.grid(row=0,column=1)
    button_load_add.grid(row=1,column=0)
    button_load_sub.grid(row=1,column=1)


####################
#Programme principal
####################

#Création du Widget parent
root = tk.Tk()

#Variable Tkinter
compteur = tk.IntVar()
gen_window_grille = tk.IntVar()
gen_window_grille.set(grille)
#Définition des raccourcis
root.bind_all('e',generation_initiale)
root.bind_all('<BackSpace>',fin_aval)
root.bind_all('<Return>',avalanche)
root.bind_all('<space>',gen_window)
root.bind_all('i',infos)
root.bind_all('v',affichage_valeurs)

#Interface graphique
root.title('Tas de Sable - Groupe 1')
canvas = tk.Canvas(root,height=HAUTEUR,width=LARGEUR,bg='black')
canvas.tag_bind("grains","<ButtonPress-1>",left_click_grain)
canvas.tag_bind("grains","<Shift-ButtonPress-1>",middle_click_grain)
canvas.tag_bind("grains","<ButtonPress-3>",right_click_grain)
generation_initiale()
button_generations = tk.Button(root,text='Génération',command=gen_window,activebackground='red')
button_avalanche = tk.Button(root,text='Start',bg='green',command=avalanche)
button_affichage_valeurs = tk.Button(root,text='Valeurs',command=affichage_valeurs)
button_stop = tk.Button(root,text='Stop',bg='red',command=fin_aval)
label_compteur = tk.Label(root,textvariable=compteur,relief='groove')
button_infos = tk.Button(root,text='Infos',bg='gray',command=infos)
button_saves = tk.Button(root,text='Saves',command=saves_txt)
button_generations.grid(row=0,column=0,columnspan=2)
button_avalanche.grid(row=4,column=0)
button_affichage_valeurs.grid(row=4,column=3)
button_stop.grid(row=4,column=1)
label_compteur.grid(row=5,column=0,columnspan=2)
button_infos.grid(row=5,column=3)
canvas.grid(row=0,rowspan=6,column=2)
button_saves.grid(row=3,column=3)

#################
#Fin du programme
#################

root.mainloop()