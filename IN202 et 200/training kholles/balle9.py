import tkinter as tk

##################
# Constantes

LARGEUR = 600
HAUTEUR = 400
rebond_stop = False
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
    global rebond_stop
    if compteur < 30:
        if not rebond_stop:
            rebond()
        else:
            rebond_stop = False
        canvas.move(mur_D,1,0)
        canvas.move(mur_G,1,0)
        canvas.move(balle[0], balle[1], balle[2])
        canvas.after(20, mouvement)


def rebond():
    """Fait rebondir la balle sur les bords du canevas"""
    global balle, rebond_stop, compteur
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if x0 <= 0 or x1 >= 600:
        balle[1] = -balle[1]
        compteur += 1
    if y0 <= 0 or y1 >= 400:
        balle[2] = -balle[2]
        compteur += 1
    line = canvas.coords(mur_G)
    overlap = canvas.find_overlapping(line[0],line[1],line[2],line[3])
    for obj in overlap:
        if obj == balle[0]:
            balle[1] = -balle[1]
            compteur += 1
            rebond_stop = True
    line = canvas.coords(mur_D)
    overlap = canvas.find_overlapping(line[0],line[1],line[2],line[3])
    for obj in overlap:
        if obj == balle[0]:
            balle[1] = -balle[1]
            compteur += 1


######################
# programme principal

# création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid()

# initialisation de la balle
balle = creer_balle()
mur_G = canvas.create_line(1,0,1,HAUTEUR,fill='white')
mur_D = canvas.create_line(150,0,150,HAUTEUR,fill='white')

# déplacement de la balle
mouvement()

# boucle principale
racine.mainloop()
