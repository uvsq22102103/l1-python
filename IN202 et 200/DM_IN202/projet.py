import PIL as pil
from PIL import Image
from PIL import ImageTk
import tkinter as tk
from tkinter.filedialog import askopenfilename
import os
import rotate_matrix as rm

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


def mat_rotate(matrice, rotation):
    '''Fonction qui prend en entrée une matrice puis la rotation désirée
    et qui retourne la matrice retournée.'''
    if rotation == 90:
        matrice = rm.anti_clockwise(matrice)
    elif rotation == 180:
        matrice = rm.anti_clockwise(matrice)
        matrice = rm.anti_clockwise(matrice)
    elif rotation == -90:
        matrice = rm.clockwise(matrice)
    return(matrice)


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
            coins[1].append([])
            for j in range(7):
                coins[0][i].append(mat[i][j])
            for j in range(18, 25):
                coins[1][i].append(mat[i][j])
        for i in range(18, 25):
            coins[2].append([])
            coins[3].append([])
            for j in range(7):
                coins[2][i-18].append(mat[i][j])
            for j in range(18, 25):
                coins[3][i-18].append(mat[i][j])
        print('\n'+affiche_mat(coins[0])+'UP left corner')
        print('\n'+affiche_mat(coins[1])+'UP right corner')
        print('\n'+affiche_mat(coins[2])+'DOWN left corner')
        print('\n'+affiche_mat(coins[3])+'DOWN right corner')
        print('\n'+affiche_mat(coin_ref)+'Référence\n\n')
        if coins[0] != coin_ref:
            print('UP Left corner should be the DOWN Right')
            mat = mat_rotate(mat, 180)
            print('Correction...')
        elif coins[1] != coin_ref:
            print('UP Right corner should be the DOWN Right')
            mat = mat_rotate(mat, 90)
            print('Correction...')
        elif coins[2] != coin_ref:
            print('DOWN Left corner should be the DOWN Right')
            mat = mat_rotate(mat, -90)
            print('Correction...')
        elif coins[3] != coin_ref:
            print('Le QR code est bien placé')
        qr_label.set(affiche_mat(mat))
        print('\nAnalyse parée\n')
    else:
        qr_label.set('Aucun QR code à checker')


def check_line():
    global mat
    print('Recherche des lignes relatives au coins...')
    line_sample = []
    # line est de 11 de long et commence par un 0


def check_qr():
    check_corner()
    # check_line()


# Initialisation du GUI

root = tk.Tk()
root.title('QR Code')
root.geometry('420x390')

# Ajout de fonctionnalités
qr_label = tk.StringVar()

button_charger = tk.Button(root, text='Charger', command=load_image, bg='gray')
button_check_qr = tk.Button(root, text='Check QR', command=check_qr, bg='gray')
label_qr = tk.Label(root, textvariable=qr_label)

button_charger.pack(side=tk.BOTTOM, ipadx=150, ipady=6)
button_check_qr.pack(side=tk.BOTTOM, ipadx=70)
label_qr.pack(pady=20)

# Maintien de la fenêtre

root.mainloop()
