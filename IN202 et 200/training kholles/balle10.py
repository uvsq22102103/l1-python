import tkinter as tk

##################
# Constantes

LARGEUR = 600
HAUTEUR = 400


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
    rebond()
    canvas.move(balle[0], balle[1], balle[2])
    balle_coords = canvas.coords(balle[0])
    balle_coords = balle_coords[0]+20,balle_coords[1]+20
    objet = canvas.coords(rectangle[0])
    zone = canvas.find_overlapping(objet[0],objet[1],objet[2],objet[3])
    for obj in zone:
        if obj == balle[0]:
            canvas.itemconfigure(balle[0],fill='white')
    objet = canvas.coords(rectangle[1])
    zone = canvas.find_overlapping(objet[0],objet[1],objet[2],objet[3])
    for obj in zone:
        if obj == balle[0]:
            canvas.itemconfigure(balle[0],fill='red')
    objet = canvas.coords(rectangle[2])
    zone = canvas.find_overlapping(objet[0],objet[1],objet[2],objet[3])
    for obj in zone:
        if obj == balle[0]:
            canvas.itemconfigure(balle[0],fill='red')
    objet = canvas.coords(rectangle[3])
    zone = canvas.find_overlapping(objet[0],objet[1],objet[2],objet[3])
    for obj in zone:
        if obj == balle[0]:
            canvas.itemconfigure(balle[0],fill='white')
    canvas.after(20, mouvement)


def rebond():
    """Fait rebondir la balle sur les bords du canevas"""
    global balle
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if x0 <= 0 or x1 >= 600:
        balle[1] = -balle[1]
    if y0 <= 0 or y1 >= 400:
        balle[2] = -balle[2]


def clic(event):
    global balle, rectangle
    j = event.x,event.y
    rectangle = []
    rectangle.append(canvas.create_rectangle(0,0,j[0],j[1],fill='red'))
    rectangle.append(canvas.create_rectangle(LARGEUR,0,j[0],j[1],fill='white'))
    rectangle.append(canvas.create_rectangle(0,HAUTEUR,j[0],j[1],fill='white'))
    rectangle.append(canvas.create_rectangle(LARGEUR,HAUTEUR,j[0],j[1],fill='red'))
    # initialisation de la balle
    balle = creer_balle()
    # déplacement de la balle
    mouvement()



######################
# programme principal

# création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid()
canvas.bind('<Button-1>',clic)

# boucle principale
racine.mainloop()
