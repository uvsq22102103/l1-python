import tkinter as tk

##################
# Constantes

LARGEUR = 600
HAUTEUR = 400
compteur = 1
type_balle = "Cercle"


###################
# Fonctions

def creer_balle(forme:str,x=LARGEUR//2,y=HAUTEUR//2):
    """Dessine la forme désirée en bleu et retourne son identifiant
     et les valeurs de déplacements dans une liste.
     \nFormes : "Cercle","Carré"."""
    dx, dy = 3, 5
    rayon = 20
    if forme == 'Cercle':
        item = canvas.create_oval((x-rayon, y-rayon),
                                  (x+rayon, y+rayon),
                                  fill="blue")
    elif forme == 'Carré':
        item = canvas.create_rectangle((x-rayon, y-rayon),
                                       (x+rayon, y+rayon),
                                       fill="blue")
    return [item, dx, dy]


def mouvement():
    """Déplace la balle et ré-appelle la fonction avec un compte-à-rebours"""
    global compteur, type_balle, balle
    rebond()
    canvas.move(balle[0], balle[1], balle[2])
    if compteur % 5 == 0:
        if type_balle == "Cercle":
            type_balle = "Carré"
        elif type_balle == "Carré":
            type_balle = "Cercle"
        coords_balle = canvas.coords(balle[0])
        canvas.delete(balle[0])
        balle = creer_balle(type_balle, x=coords_balle[0], y=coords_balle[1])
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


######################
# programme principal

# création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid()

# initialisation de la balle
balle = creer_balle(type_balle)

# déplacement de la balle
mouvement()

# boucle principale
racine.mainloop()
