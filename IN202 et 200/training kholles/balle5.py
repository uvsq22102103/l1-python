import tkinter as tk
import random as rd

##################
# Constantes et variables

LARGEUR = 600
HAUTEUR = 400
LIGNE = [LARGEUR//2,0,LARGEUR//2,HAUTEUR]
ligne = True
compteur = 0

###################
# Fonctions

def creer_balle():
    """Dessine un disque bleu et retourne son identifiant
     et les valeurs de déplacements dans une liste"""
    x, y = 200 , HAUTEUR // 2
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),
                                (x+rayon, y+rayon),
                                fill="blue")
    return [cercle, dx, dy]


def mouvement():
    global ligne
    """Déplace la balle et ré-appelle la fonction avec un compte-à-rebours"""
    if compteur < 30:
        rebond()
        canvas.move(balle[0], balle[1], balle[2])
        canvas.after(20, mouvement)
        if rd.randint(0,100) < 10:
            if ligne:
                canvas.itemconfigure(ligne_V,state='hidden')
                ligne = False
            elif not ligne:
                canvas.itemconfigure(ligne_V,state='normal')
                ligne = True


def rebond():
    """Fait rebondir la balle sur les bords du canevas"""
    global balle, compteur
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if x0 <= 0 or x1 >= 600:
        balle[1] = -balle[1]
        compteur += 1
    if y0 <= 0 or y1 >= 400:
        balle[2] = -balle[2]
        compteur += 1
    if ligne:
        ligne_overlaping = canvas.find_overlapping(LIGNE[0],LIGNE[1],LIGNE[2],LIGNE[3])
        for obj in ligne_overlaping:
            if obj == balle[0]:
                balle[1] = -balle[1]
                compteur += 1


######################
# programme principal

# création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid()

# initialisation des objets
balle = creer_balle()
ligne_V = canvas.create_line(LIGNE[0],LIGNE[1],LIGNE[2],LIGNE[3],fill='white')

# déplacement de la balle
mouvement()

# boucle principale
racine.mainloop()
