import tkinter as tk
from animal import Animal
import random as rd


# CONSTANTES ET VARIABLES #
HAUTEUR = 500
LARGEUR = 500
PROIES = 10
PREDATEURS = 0
RAYON = int(HAUTEUR/30)
###########################
# FONCTIONS #


def placement_animaux():
    global l_proies, l_preds
    l_proies = []
    l_preds = []
    l_placements = []
    for i in range(PROIES):
        coords = ()
        while coords in l_placements or coords == ():
            coords = (rd.randint(1, 30), rd.randint(1, 30))
        l_placements.append(coords)
        l_proies.append(Animal("proie", coords))
    for i in range(PREDATEURS):
        coords = ()
        while coords in l_placements or coords == ():
            coords = (rd.randint(1, 30), rd.randint(1, 30))
        l_preds.append(Animal("predateur", coords))
    for proie in l_proies:
        proie.show(canvas_env, RAYON)
    for pred in l_preds:
        pred.show(canvas_env, RAYON)


def return_placement(liste):
    output = []
    for animal in liste:
        output.append((animal.x, animal.y))
    return output


def simulation():
    global l_proies, l_preds, after_id
    for proie in l_proies:
        l_placements = return_placement(l_proies)
        proie.move(l_placements)
        proie.update(canvas_env, RAYON)
    after_id = canvas_env.after(500, simulation)


def stop_simul():
    canvas_env.after_cancel(after_id)


#############

root = tk.Tk()
root.title('Prédateurs & Proies')

canvas_env = tk.Canvas(root, width=LARGEUR, height=HAUTEUR, bg='#1F800D')
button_creation = tk.Button(root, text="Création", command=placement_animaux)
button_simulation = tk.Button(root, text="Simuler", command=simulation)
button_stop = tk.Button(root, text="Stop", command=stop_simul)

canvas_env.grid(column=0, columnspan=3)
button_creation.grid(row=1)
button_simulation.grid(row=1, column=1)
button_stop.grid(row=1, column=2)

root.mainloop()
