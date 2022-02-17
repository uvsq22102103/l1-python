import tkinter as tk
import time

def comptage():
    compteur = 0
    for i in range(200):
        compteur += 1
        texte.set(compteur)
        root.update()
        time.sleep(1)

root = tk.Tk()
texte = tk.IntVar()

boutton_compteur = tk.Button(root,text='Compteur',command=comptage)
label_dynamique = tk.Label(root,textvariable=texte)

boutton_compteur.grid(row=0,column=0)
label_dynamique.grid(row=0,column=1)

root.mainloop()