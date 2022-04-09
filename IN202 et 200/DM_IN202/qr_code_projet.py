# noir = 0
# blanc  = 1
from tracemalloc import stop
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


def squellette():
    matrice =loading("coin.png")
    return matrice


def check_coin(matrice):
    matrice = loading(matrice)
    test = squellette()
    chek = 0

    for i in range (8):
        if matrice[i][:8] == test[i] and matrice[-i+(-1)][:8] == test[i] and matrice[i][17:] == test[i] [: :-1] :
            chek  = True
            pass
        else: 
            print("ce n'est pa un bon carré" )
            matrice = rotate(matrice)
    if chek == True :        
        print("les qr code est dans la bonne position")


def check_alternance(matrice):
    alternance = [1,0,1,0,1,0,1,0,1,0,1]
    matrice = loading(matrice)
    verif = True
    for i in range (11):
        if matrice[6][7+i] == alternance[i] and matrice[7+i][6] == alternance[i]  :
            verif = True
            print("ca marche")
        else : 
            print("nope")
            matrice = rotate(matrice)

 
        


def rotate(matrice):
    mat=[]
    for i in range(nbrCol(matrice)):
        ligne = []
        for j in range(nbrLig(matrice)):
            ligne.append(matrice[j][i])
        ligne.reverse()
        mat.append(ligne)
    matrice = list(mat)
    return matrice


def decode(l):
    d1,d2,d3,d4,p1,p2,p3 = l
    c = [True,True,True]
    correction = ""
    if p1 != ((d1 + d2 + d4) % 2):
        c[0] = False
    if p2 != ((d1 + d3 + d4) % 2):
        c[1] = False
    if p3 != ((d2 + d3 + d4) % 2):
        c[2] = False
    
    if False in c:
        if c.count(False) == 3:
            d4 = 1 - d4
            correction = "d4"
        elif c.count(False) == 2:
            if c[0] == False and c[1] == False:
                d1 = 1 - d1
                correction = "d1"
            elif c[0] == False and c[2] == False:
                d2 = 1 - d2
                correction = "d2"
            elif c[1] == False and c[2] == False:
                d3 = 1 - d3
                correction = "d3"
        elif c.count(False) == 1 :
            if c[0] == False:
                p1 = 1 - p1
                correction = "p1"
            if c[1] == False:
                p2 = 1 - p2
                correction = "p2"
            if c[2] == False:
                p3 = 1 - p3
                correction = "p3"
    else : 
        correction = "aucune correction"
    l = d1,d2,d3,d4,p1,p2,p3
    d = d1,d2,d3,d4
    print (correction)
    return(d)
a = decode([0, 1, 1, 0, 1, 1, 0])
print(a)




# check_alternance("qr_code_ssfiltre_ascii_rotation.png")
