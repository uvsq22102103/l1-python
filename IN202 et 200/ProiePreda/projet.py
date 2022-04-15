import tkinter as tk
import random as rd
import time
import itertools as it

# VARIABLES ET CONSTANTES #

HAUTEUR, LARGEUR = 700, 700 # Dimension HUD
GRILLE = 30 # Taille de l'environnement des entités
DIST = HAUTEUR/GRILLE
PROIES = 10 # Nombre de Proies dans une création
PREDATEURS = 5 # Nombre de Prédateurs dans une création
ENTITY = PROIES + PREDATEURS
compteur = 0
simulation_state = False

###########################
# CLASS #

class Animal:
    def __init__(self, status: str, coords: tuple):
        if status == "proie":
            self.vie = 5
        else:
            self.vie = 6
        self.status = status
        self.coords = coords
        self.baby = 0
        self.obj = apparition(self)
    
    def move(self, env: list):
        if self.vie > 0:
            movs = []
            for i in range(3):
                i -= 1
                for j in range(3):
                    j -= 1
                    ij = (i*DIST, j*DIST)
                    p_mov = (self.coords[0] + i, self.coords[1] + j)
                    if p_mov not in env or p_mov == self.coords:
                        if 0 <= int(p_mov[0]) <= 29 and 0 <= int(p_mov[1]) <= 29:
                            movs.append((ij,p_mov))
            mov = rd.choice(movs)
            canvas.move(self.obj,mov[0][0],mov[0][1])
            self.coords = mov[1]
            if self.vie != 6:
                self.vie -= 1
        else:
            canvas.delete(self.obj)
            self.status = "dead"
    
    def breed(self, copinage: list):
        if self.baby <= 1:
            matchs = []
            for i in range(3):
                i -= 1
                for j in range(3):
                    j -= 1
                    coords = (self.coords[0]-i, self.coords[1]-j)
                    try:
                        if coords != self.coords:
                            match = copinage.index(coords)
                            matchs.append((match,coords))
                    except ValueError:
                        pass
            if 0 < len(matchs) < 8:
                match = rd.choice(matchs)
                l_proies[match[0]].baby += 1
                self.baby += 1
                l_bebe.append(Animal("proie",match[1]))
                canvas.update()


#########
# FONCTIONS #

def apparition(Animal):
    x, y = Animal.coords
    if Animal.status == "proie":
        obj = canvas.create_oval(x*DIST,y*DIST,x*DIST+DIST,y*DIST+DIST,fill="#F6E1BE")
    else:
        obj = canvas.create_oval(x*DIST,y*DIST,x*DIST+DIST,y*DIST+DIST,fill="#E50B0B")
    return obj


def create():
    global l_proies, l_preds
    places = [] # Variable de référencement du placement de chaques entités
    l_proies = []
    l_preds =  []
    for i in range(PROIES):
        coords = (rd.randint(0,29),rd.randint(0,29))
        while coords in places:
            coords = (rd.randint(0,29),rd.randint(0,29))
        places.append(coords)
        l_proies.append(Animal("proie",coords))
    for i in range(PREDATEURS):
        coords = (rd.randint(0,29),rd.randint(0,29))
        while coords in places:
            coords = (rd.randint(0,29),rd.randint(0,29))
        places.append(coords)
        l_proies.append(Animal("predateur",coords))


def placements(liste:list):
    output = []
    for animal in liste:
        output.append(animal.coords)
    return output


def spawn(nombre: int, typage: str):
    global l_proies, l_preds
    if typage == "proie":
        for i in range(nombre):
            reroll = 0
            places = placements(l_proies+l_preds)
            coords = (rd.randint(0,29), rd.randint(0,29))
            while coords in places and reroll < 10:
                coords = (rd.randint(0,29), rd.randint(0,29))
                reroll += 1
            l_proies.append(Animal("proie", coords))
    elif typage == "predateur":
        for i in range(nombre):
            reroll = 0
            places = placements(l_proies+l_preds)
            coords = (rd.randint(0,29), rd.randint(0,29))
            while coords in places and reroll < 10:
                coords = (rd.randint(0,29), rd.randint(0,29))
                reroll += 1
            l_preds.append(Animal("predateur", coords))


def check_dead():
    global l_proies, l_preds
    compteur_morts = 0
    for i in range(len(l_proies)):
        if l_proies[i-compteur_morts].status == "dead":
            del l_proies[i-compteur_morts]
            compteur_morts += 1


def tour():
    global l_proies, l_preds, compteur, after_id, l_bebe
    start = time.time()
    l_bebe = []
    for proie in l_proies:
        if simulation_state:
            proie.move(placements(l_proies+l_preds))
            proie.breed(placements(l_proies))
            canvas.update()
            #time.sleep(0.05)
    l_proies += l_bebe
    for pred in l_preds:
        if simulation_state:
            pred.move(placements(l_proies+l_preds))
            canvas.update()
            #time.sleep(0.05)
    compteur += 1
    print("Tour n°"+str(compteur)+" terminé.")
    if simulation_state:
        spawn(3,"proie")
        check_dead()
        stop = time.time()
        print("temps = ",round(stop-start,2)," sec")
        after_id = canvas.after(50, tour)


def simul():
    global simulation_state
    if not simulation_state:
        simulation_state = True
        print("Démarrage Simulation :")
        tour()
    else:
        simulation_state = False
        canvas.after_cancel(after_id)
        print("Simulation en pause;")


def check_places():
    print(placements(l_proies+l_preds))


#############

root = tk.Tk()

canvas = tk.Canvas(root,height=HAUTEUR,width=LARGEUR, bg="#278410")
button_create = tk.Button(root,text="Create",command=create)
button_move = tk.Button(root,text="Start/Stop",command=simul)
button_check = tk.Button(root,text="Check",command=check_places)
canvas.grid(column=0,columnspan=4)
button_create.grid(row=1)
button_move.grid(row=1,column=1)
button_check.grid(row=1,column=2)

root.mainloop()