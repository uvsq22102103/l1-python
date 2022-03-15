import random as rd

dir_input = '/home/aymeric/Documents/uvsq-github/l1-python/IN202 et 200/TD_fichiers/words.txt'
dir_output = '/home/aymeric/Documents/uvsq-github/l1-python/IN202 et 200/TD_fichiers/wordsn.txt'
dir_repertoire = '/home/aymeric/Documents/uvsq-github/l1-python/IN202 et 200/TD_fichiers/'


def charger(nom_fichier):
    global dir, notes
    dir = nom_fichier
    fichier = open(file=nom_fichier, mode='r')
    notes = fichier.readlines()
    fichier.close()


def nb_lignes():
    return(len(notes))


def ecrit_liste_mots(n):
    lignes = []
    tri = []
    output = str()
    for ligne in notes:
        lignes.append(ligne.replace('\n',''))
    for line in lignes:
        if len(line) == n:
            tri.append(line)
    for i in tri:
        output += i + '\n'
    fichier_output = open(dir_output, mode='w')
    fichier_output.write(output)
    fichier_output.close()
    return(len(tri))


def melange_mots(fichier):
    output = str()
    dir_melange = dir_repertoire + fichier
    fichier = open(file=dir_melange, mode='r')
    lignes = fichier.readlines()
    fichier.close()
    rd.shuffle(lignes)
    fichier_output = open(file=dir_melange[0:-3]+'mel', mode='w')
    for i in lignes:
        output += i
    fichier_output.write(output)
    fichier_output.close()


def compare_mots(m1, m2):
    '''m1 et m2 doivent être de même taille !'''
    m1, m2 = m2, m1
    m1 = m1.strip('\n')
    m2 = m2.strip('\n')
    liste = []
    for i in range(len(m1)):
        if m1[i] == m2[i]:
            liste.append(1)
        elif m1[i] in m2:
            liste.append(2)
        else:
            liste.append(0)
    return liste


print(compare_mots('vvvvv\n', 'vivre\n'))
