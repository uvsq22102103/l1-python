import tkinter as tk

taille_fenetre = 100 #Taille de la fenêtre de recherche
min_match = 3 #Taille du plus petit match permis


def match_size(mot,i,j): #renvoie la valeur du plus grand sous-mot commun,
                       #dans le mot aux positions position i et j avec j < i
    k = 0
    while i+k < len(mot) and mot[j+k] == mot[i+k]:
        k+=1
    return k

def max_match(mot,i): #renvoie le couple (position,taille) du plus grand match 
                      #trouvé dans mot à partir de la position i
    j = max(0,i-taille_fenetre)  #première position où chercher un match
    max_match = (0,0)
    while j < i: #on cherche un match dans la fenetre de recherche
        size = match_size(mot, i, j)
        if size > max_match[1]:
            max_match = (j, size)
        j += 1
    return max_match


def compresse():
    texte_a_compresser = entree.get()
    texte_compresse = [] #cette liste doit etre étendue pour contenir le texte compressé
    #construction du code LZ77
    i = 0
    while i < len(texte_a_compresser): #pour chaque lettre du texte
        match = max_match(texte_a_compresser,i)
        if match[1] < min_match:
            texte_compresse.append(texte_a_compresser[i])
            i+=1
        else:
            texte_compresse.append((i-match[0],match[1]))
            i += match[1]
        #à compléter en utilisant les fonctions précédemment codées
    taille_origine = len(texte_a_compresser)
    taille_sortie = taille(texte_compresse)
    str_out = str(texte_compresse)
    str_out += "\nTaille Origine : "+ str(taille_origine) + "\nTaille Sortie : " + str(taille_sortie)
    str_out += "\nRation : " + str(round(taille_origine/taille_sortie,2))
    affichage_compression.config(text = str_out) #affichage du texte compressé 
    
    

def taille(liste_LZ):# calcule la taille de la liste. Un caractère compte 1 et 
                                   # une paire d'entier compte 2
    taille = 0
    for elem in liste_LZ:
        taille += 1 if type(elem) == str else 2
    return taille

    
def match2():
    global min_match
    min_match = 2
    
def match3():
    global min_match
    min_match = 3

racine = tk.Tk()
racine.title("Compression de texte")

entree = tk.Entry(racine, width = 30,font = ("helvetica", "20"))
entree.grid(row = 1, column = 0)

affichage_compression = tk.Label(racine, font = ("helvetica", "20"), width = 50)
affichage_compression.grid(row = 2, column = 0, columnspan = 2)


affichage_binaire = tk.Label(racine, font = ("helvetica", "20"), width = 50)
affichage_binaire.grid(row = 6, column = 0, columnspan = 2)


bouton_compresser = tk.Button(racine, text = "Compresser", command = compresse, font = ("helvetica", "30"))
bouton_compresser.grid(row = 1, column = 1)



racine.mainloop()