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
    x, y = LARGEUR // 2, 300
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
        canvas.move(ligne_H,0,1)
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
    line = canvas.coords(ligne_H)
    overlap_line = canvas.find_overlapping(line[0],line[1],line[2],line[3])
    for obj in overlap_line:
        if obj == balle[0]:
            balle[2] = -balle[2]
            canvas.move(ligne_H,0,-50)
            compteur += 1



######################
# programme principal

# création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid()

# initialisation de la balle
balle = creer_balle()
ligne_H = canvas.create_line(0,HAUTEUR//2,LARGEUR,HAUTEUR//2,fill='white')

# déplacement de la balle
mouvement()

# boucle principale
racine.mainloop()
