import PIL as pil
from PIL import Image
from PIL import ImageTk

def nbrCol(matrice):
    return(len(matrice[0]))

def nbrLig(matrice):
    return len(matrice)

def saving(matPix, filename):#sauvegarde l'image contenue dans matpix dans le fichier filename
							 #utiliser une extension png pour que la fonction fonctionne sans perte d'information
    toSave=pil.Image.new(mode = "1", size = (nbrCol(matPix),nbrLig(matPix)))
    for i in range(nbrLig(matPix)):
        for j in range(nbrCol(matPix)):
            toSave.putpixel((j,i),matPix[i][j])
    toSave.save(filename)

def loading(filename):#charge le fichier image filename et renvoie une matrice de 0 et de 1 qui représente 
					  #l'image en noir et blanc
    toLoad=pil.Image.open(filename)
    mat=[[0]*toLoad.size[0] for k in range(toLoad.size[1])]
    for i in range(toLoad.size[1]):
        for j in range(toLoad.size[0]):
            mat[i][j]= 0 if toLoad.getpixel((j,i)) == 0 else 1
    return mat

def affiche_mat(matrice):
    for i in matrice:
        print(i)

def qr_coin():
    coin = []
    for i in range(9):
        coin.append([])
        for j in range(9):
            coin[i].append(0)
    for i in range(7):
        i += 1
        for j in range(7):
            j += 1
            coin[i][j] = 1
    for i in range(5):
        i += 2
        for j in range(5):
            j += 2
            coin[i][j] = 0
    for i in range(3):
        i += 3
        for j in range(3):
            j += 3
            coin[i][j] = 1
    return coin

affiche_mat(qr_coin())