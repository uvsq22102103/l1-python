import tkinter as tk
import random as rd
from tkinter.constants import X

objets = []
couleur1 = "red"

def cercle():
    x = rd.randint(0,550)
    y = rd.randint(0,550)
    objets.append(canvas.create_oval((x,y),(x+50,y+50),fill=couleur1))
def carre():
    x = rd.randint(0,550)
    y = rd.randint(0,550)
    objets.append((canvas.create_rectangle((x,y),(x+50,y+50),fill=couleur1)))

def undo_canvas():
    if len(objets) != 0 :    
        if canvas.type(objets[-1]) == 'line':
            canvas.delete(objets[-1])
            del(objets[-1])
            canvas.delete(objets[-1])
            del(objets[-1])
        else:
            canvas.delete(objets[-1])
            del(objets[-1])
    else:
        print('\n\nError:\nthere is no objects on the canvas')
def croix():
    x = rd.randint(0,550)
    y = rd.randint(0,550)
    objets.append(canvas.create_line((x-50,y),(x+50,y),width=5,fill= couleur1))
    objets.append(canvas.create_line((x,y-50),(x,y+50),width=5,fill= couleur1))


def evangelion():
    x = rd.randint(0,550)
    y = rd.randint(0,550)
    objets.append(canvas.create_line((x-50,y),(x+50,y),width=10,fill= couleur1))
    objets.append(canvas.create_line((x,y-50),(x,y+100),width=10,fill= couleur1))

def color(couleur):
    global couleur1
    couleur1 = couleur



root = tk.Tk()
root.title("Mon dessin")

canvas = tk.Canvas(root,width=550 , height=550, bg= "black")
button_carre= tk.Button(root, text= "Carré",command= carre)
button_cercle= tk.Button(root, text = "Cercle",command= cercle)
button_croix= tk.Button(root, text = "Croix",command= croix)
button_evangelion= tk.Button(root, text="Evangelion", command= evangelion)
button_couleur= tk.Button(root, text = "Choisir une couleur")
button_undo= tk.Button(root,text= "Undo", command=undo_canvas)

#button .b -bg [tk_chooseColor -initialcolor gray -title "Choose color"]

canvas.grid(row=1,rowspan=3,column=1,columnspan=2)
button_carre.grid(row=2,column=0)
button_evangelion.grid(row=4,column=0)
button_couleur.grid(row=0, column=1)
button_cercle.grid(row=1,column=0)
button_croix.grid(row=3,column=0)
button_undo.grid(row=0,column=2)

if couleur1 == "":
    couleur1 = "red"

root.mainloop()