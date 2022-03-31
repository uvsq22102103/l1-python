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
    x, y = 100, HAUTEUR // 2
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),
                                (x+rayon, y+rayon),
                                fill="blue")
    return [cercle, dx, dy]


def mouvement():
    """Déplace la balle et ré-appelle la fonction avec un compte-à-rebours"""
    if compteur < 30:
        rebond()
        canvas.move(balle[0], balle[1], balle[2])
        canvas.move(trait,-1,0)
        canvas.after(20, mouvement)


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
    coords_trait = canvas.coords(trait)
    zone_trait = canvas.find_overlapping(coords_trait[0],coords_trait[1],coords_trait[2],coords_trait[3])
    for obj in zone_trait:
        if obj == balle[0]:
            balle[1] = -balle[1]
            canvas.move(trait,50,0)
            compteur += 1


######################
# programme principal

# création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid()

trait = canvas.create_line(LARGEUR/2,0,LARGEUR/2,HAUTEUR,fill='white')

# initialisation de la balle
balle = creer_balle()

# déplacement de la balle
mouvement()

# boucle principale
racine.mainloop()
