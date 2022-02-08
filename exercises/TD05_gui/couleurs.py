import random as rd
import tkinter as tk

dimension = 255

def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def get_rd_color():
    r,g,b = rd.randint(0,255),rd.randint(0,255),rd.randint(0,255)
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def draw_pixel(i,j,color):
    canvas.create_line(i,j,i+1,j,fill= color)

def aleatoire():
    global dimension
    for x in range(dimension):
        for y in range(dimension):
            draw_pixel(x,y,get_rd_color())

def dg_gris():
    global dimension
    for y in range(dimension):
        color = 0
        for x in range(dimension):
            draw_pixel(x,y,get_color(color,color,color))
            color += 1

def dg_2d():
    global dimension
    b = 0
    for y in range(dimension):
        r = 0
        for x in range(dimension):
            draw_pixel(x,y,get_color(r,0,b))
            r += 1
        b += 1


#Invocation
root = tk.Tk()

canvas = tk.Canvas(root, width=200, height= 200, bg = "Black")
button_aleatoire = tk.Button(root, text="Aléatoire",command= aleatoire)
button_DG = tk.Button(root, text="Dégradé Gris",command= dg_gris)
button_2D = tk.Button(root, text="Dégradé 2D",command= dg_2d)

#Placement

canvas.grid(row=1,rowspan=3,column=1)
button_aleatoire.grid(row=1,column=0)
button_2D.grid(row=3,column=0)
button_DG.grid(row=2,column=0)

root.mainloop()