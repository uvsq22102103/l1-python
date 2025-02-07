from asyncore import compact_traceback
import tkinter as tk

##################
# Constantes

LARGEUR = 600
HAUTEUR = 400
compteur = 0


###################
# Fonctions

def creer_balle():
    """Dessine un disque bleu et retourne son identifiant
     et les valeurs de déplacements dans une liste"""
    x, y = LARGEUR // 2, HAUTEUR // 2
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),
                                (x+rayon, y+rayon),
                                fill="blue")
    return [cercle, dx, dy]


def mouvement():
    """Déplace la balle et ré-appelle la fonction avec un compte-à-rebours"""
    if compteur < 5:
        rebond()
        canvas.move(balle[0], balle[1], balle[2])
        canvas.after(20, mouvement)


def change_forme(compteur):
    if compteur % 5 == 0 and compteur != 0:
        obj = canvas.type(balle[0])
        coords = canvas.coords(balle[0])
        canvas.delete(balle[0])
        if obj == 'oval':
            balle[0] = canvas.create_rectangle(coords[0],coords[1],coords[2],coords[3],fill='yellow')
        elif obj == 'rectangle':
            balle[0] = canvas.create_oval(coords[0],coords[1],coords[2],coords[3],fill='blue')


def rebond():
    """Fait rebondir la balle sur les bords du canevas"""
    global balle, compteur
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if x0 <= 0 or x1 >= 600:
        balle[1] = -balle[1]
        compteur += 1
        change_forme(compteur)
    if y0 <= 0 or y1 >= 400:
        balle[2] = -balle[2]
        compteur += 1
        change_forme(compteur)


######################
# programme principal

# création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid()

# initialisation de la balle
balle = creer_balle()

# déplacement de la balle
mouvement()

# boucle principale
racine.mainloop()
