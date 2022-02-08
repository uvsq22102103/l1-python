import tkinter as tk
import random as rd
cote = 280
nb = int(input('Cb de cercles'))
def random_color():
    r,g,b = rd.randint(0,255),rd.randint(0,255),rd.randint(0,255)
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def create_oval(dimension):
    canvas.create_oval(300+dimension,300+dimension,300-dimension,300-dimension,fill=random_color())

root = tk.Tk()
root.title('LA CIBLE QUI VA DROIT AU COEUR')
canvas = tk.Canvas(root,height=600,width=600,bg='black')
canvas.grid(row=0,column=0)

iterations = int(cote/nb)
for i in range(nb):
    create_oval(cote)
    cote -= iterations

root.mainloop()