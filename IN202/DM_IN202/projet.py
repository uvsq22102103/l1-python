import PIL as pil
from PIL import Image
from PIL import ImageTk
import tkinter as tk
from tkinter.filedialog import askopenfilename
import os

check = False


def nbrCol(matrice):
    return(len(matrice[0]))


def nbrLig(matrice):
    return len(matrice)


def saving(matPix, filename):
    # sauvegarde l'image contenue dans matpix dans le fichier filename
	# utiliser une extension png pour que la fonction fonctionne sans perte d'information
    toSave = pil.Image.new(mode= "1",size= (nbrCol(matPix),nbrLig(matPix)))
    for i in range(nbrLig(matPix)):
        for j in range(nbrCol(matPix)):
            toSave.putpixel((j,i),matPix[i][j])
    toSave.save(filename)


def loading(filename):
    # charge le fichier image filename et renvoie une matrice de 0 et de 1 qui représente 
    # l'image en noir et blanc
    global dimension_qr
    toLoad = pil.Image.open(filename)
    mat = [[0]*toLoad.size[0] for k in range(toLoad.size[1])]
    dimension_qr = toLoad.size[1], toLoad.size[0]
    for i in range(dimension_qr[0]):
        for j in range(dimension_qr[1]):
            mat[i][j] = 1 if toLoad.getpixel((j,i)) == 0 else 0
    return mat


def affiche_mat(matrice):
    label = str()
    for i in matrice:
        for y in i:
            label += str(y)+' '
        label += '\n'
    return label


def qr_coin():
    '''Cette fonction ne prend rien en argument et retourne un coin de QR code
    sous forme de matrice ! '''
    coin = []
    for i in range(7):
        coin.append([])
        for j in range(7):
            coin[i].append(1)
    for i in range(5):
        i += 1
        for j in range(5):
            j += 1
            coin[i][j] = 0
    for i in range(3):
        i += 2
        for j in range(3):
            j += 2
            coin[i][j] = 1
    return coin


def dir_image():
    file_dir = askopenfilename(initialdir=os.path.realpath(__file__)[0:-9])
    return file_dir


def load_image():
    global mat, check
    mat = loading(dir_image())
    qr_label.set(affiche_mat(mat))
    if dimension_qr[0] == 25 and dimension_qr[1] == 25:
        check = True


def check_corner():
    global check, mat
    if check:
        coin_ref = qr_coin()
        coins = [[], [], [], []]
        for i in range(7):
            coins[0].append([])
            for j in range(7):
                coins[0][i].append(mat[i][j])
        for i in range(7):
            coins[1].append([])
            for j in range(18, 25):
                coins[1][i].append(mat[i][j])
        for i in range(18, 25):
            coins[2].append([])
            for j in range(7):
                coins[2][i-18].append(mat[i][j])
        for i in range(18, 25):
            coins[3].append([])
            for j in range(18, 25):
                coins[3][i-18].append(mat[i][j])
        print('\n'+affiche_mat(coins[0])+'UP left corner')
        print('\n'+affiche_mat(coins[1])+'UP right corner')
        print('\n'+affiche_mat(coins[2])+'DOWN left corner')
        print('\n'+affiche_mat(coins[3])+'DOWN right corner')
        print('\n'+affiche_mat(coin_ref)+'Référence\n\n')
        if coins[0] != coin_ref:
            print('UP Left corner should be the DOWN Right')
        elif coins[1] != coin_ref:
            print('UP Right corner should be the DOWN Right')
        elif coins[2] != coin_ref:
            print('DOWN Left corner should be the DOWN Right')
        elif coins[3] != coin_ref:
            print('Le QR code est bien placé')
    else:
        qr_label.set('Aucun QR code à checker')


# Initialisation du GUI

root = tk.Tk()
root.title('QR Code')
root.geometry('500x500')

# Ajout de fonctionnalités
qr_label = tk.StringVar()

button_charger = tk.Button(root, text='Charger', command=load_image)
button_check_corner = tk.Button(root,text='Check corner', command=check_corner)
label_qr = tk.Label(root, textvariable=qr_label)

button_charger.pack(side=tk.BOTTOM)
button_check_corner.pack(side=tk.BOTTOM)
label_qr.pack(pady=20)

# Maintien de la fenêtre

root.mainloop()
