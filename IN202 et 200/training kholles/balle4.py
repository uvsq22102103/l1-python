import tkinter as tk

##################
# Constantes

LARGEUR = 600
HAUTEUR = 400
compteur = 0
compteur_change_balle = 0


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
    if compteur < 30:
        rebond()
        canvas.move(balle[0], balle[1], balle[2])
        canvas.after(20, mouvement)


def change_balle():
    global compteur_change_balle
    if compteur % 5 == 0 and compteur != 0:
        balle_coords = canvas.coords(balle[0])
        canvas.delete(balle[0])
        if compteur_change_balle % 2 == 0:
            balle[0] = canvas.create_rectangle(balle_coords[0],balle_coords[1],balle_coords[2],balle_coords[3],fill='green')
        elif compteur_change_balle % 2 != 0:
            balle[0] = canvas.create_oval(balle_coords[0],balle_coords[1],balle_coords[2],balle_coords[3],fill='blue')
        compteur_change_balle += 1



def rebond():
    """Fait rebondir la balle sur les bords du canevas"""
    global balle, compteur
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if x0 <= 0 or x1 >= 600:
        balle[1] = -balle[1]
        compteur += 1
        change_balle()
    if y0 <= 0 or y1 >= 400:
        balle[2] = -balle[2]
        compteur += 1
        change_balle()


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
