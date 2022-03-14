import PIL as pil
from PIL import Image
from PIL import ImageTk


def nbrCol(matrice):
    return(len(matrice[0]))


def nbrLig(matrice):
    return len(matrice)


def saving(matPix, filename):
    #sauvegarde l'image contenue dans matpix dans le fichier filename
	#utiliser une extension png pour que la fonction fonctionne sans perte d'information
    toSave = pil.Image.new(mode= "1",size= (nbrCol(matPix),nbrLig(matPix)))
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
    '''Cette fonction ne prend rien en argument et retourne un coin de QR code
    sous forme de matrice ! '''
    coin = []
    size = 9
    compteur = 0
    while size >= 3:
        if compteur == 1 or compteur == 3:
            nombre = 1
        else:
            nombre = 0
        for i in range(size):
            if size == 9:
                coin.append([])
            else:
                i += compteur
            for j in range(size):
                if size == 9:
                    coin[i].append(nombre)
                else:
                    j += compteur
                    coin[i][j] = nombre
        size -= 2
        compteur += 1
    return coin


affiche_mat(qr_coin())