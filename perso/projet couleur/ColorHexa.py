######################
#import des librairies
######################

import tkinter as tk

#################
#Variables utiles
#################

alphabet = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
copiable = str()

#########################
#Définition des fonctions
#########################

def button_pressed():
    global copiable
    rgb1 = hexa_to_rgb(entry1_var.get())
    rgb2 = hexa_to_rgb(entry2_var.get())
    couleurs_rgb = degrade(rgb1,rgb2,entry3_var.get())
    couleurs = rgb_to_hexa(couleurs_rgb)
    texte = '\n\n'
    copiable = str()
    for i in couleurs:
        texte += i+' '
        copiable += i+' '
    texte += '\n\n'
    output_str.set(texte)
    button_copy.grid(row=4,column=2)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(copiable)
    root.update()

def hexa_to_rgb(entry):
    entry = entry.replace('#','')
    liste = []
    liste2 = []
    liste.append(entry[0]+entry[1])
    liste.append(entry[2]+entry[3])
    liste.append(entry[4]+entry[5])
    for hexa in liste:
        liste2.append(alphabet.index(hexa[0])*16+alphabet.index(hexa[1]))
    print(liste2)
    return(liste2)

def degrade(color1,color2,etapes):
    liste = []
    liste1 = []
    for i in range(3):
        liste.append([])
        if color1[i] > color2[i]:
            diff = color1[i]-color2[i]
            gain = diff / (etapes-1)
            for y in range(etapes):
                liste[i].append(int(color2[i]+gain*(y)))
            liste[i].reverse()
        elif color1[i] < color2[i]:
            diff = color2[i]-color1[i]
            gain = diff / (etapes-1)
            for y in range(etapes):
                liste[i].append(int(color1[i]+gain*(y)))
        else:
            for y in range(etapes):
                liste[i].append(int(color1[i]))
    print(liste)
    for i in range(etapes):
        liste1.append([])
        liste1[i].append(liste[0][i])
        liste1[i].append(liste[1][i])
        liste1[i].append(liste[2][i])
    print(liste1)
    return(liste1)

def rgb_to_hexa(colors):
    liste = []
    for rgb in colors:
        red = hex(rgb[0]).replace('0x','')
        green = hex(rgb[1]).replace('0x','')
        blue = hex(rgb[2]).replace('0x','')
        if len(red) == 1:
            red = '0' + red
        elif len(green) == 1:
            green = '0' + green
        elif len(blue) == 1:
            blue = '0' + blue
        liste.append('#'+red+green+blue)
    print(liste)
    return(liste)

####################
#Programme principal
####################

root = tk.Tk()
root.title('ColorHexa - v0.1')

entry1_var = tk.StringVar()
entry2_var = tk.StringVar()
entry3_var = tk.IntVar()
output_str = tk.StringVar()
output_str.set('\n\n\n\nThe result is suppose to be print right here\n\n\n\n')
entry1_var.set('Starting color')
entry2_var.set('Ending color')
entry3_var.set(5)

label = tk.Label(root,text='Programme de dégradé de couleurs :')
label_sortie = tk.Label(root,textvariable=output_str)
entry1 = tk.Entry(root,textvariable=entry1_var)
entry2 = tk.Entry(root,textvariable=entry2_var)
entry3 = tk.Entry(root,textvariable=entry3_var)
button = tk.Button(root,text='Process',command=button_pressed)
button_copy = tk.Button(root,text='Copy',command=copy_to_clipboard)

label.grid(row=0,column=1)
label_sortie.grid(row=1,column=1)
entry1.grid(row=2,column=0)
entry2.grid(row=2,column=2)
entry3.grid(row=3,column=1)
button.grid(row=4,column=1)

#################
#Fin du programme
#################

root.mainloop()