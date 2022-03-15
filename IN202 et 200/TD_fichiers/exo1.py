# from tkinter import filedialog

# dir = filedialog.askopenfilename()
dir_input = '/home/aymeric/Documents/uvsq-github/l1-python/IN202 et 200/TD_fichiers/notes.txt'
dir_output = '/home/aymeric/Documents/uvsq-github/l1-python/IN202 et 200/TD_fichiers/moyenne.txt'

fichier = open(file=dir_input, mode='r')
lignes = fichier.readlines()
fichier.close()
moyennes = []
output = str()

for i in range(len(lignes)):
    lignes[i] = lignes[i].replace('\n', '')
    lignes[i] = lignes[i].split()
    calcul = 0
    for j in range(len(lignes[i])-1):
        j += 1
        calcul += int(lignes[i][j])
    moyennes.append(calcul//(len(lignes)-2))

compteur = 0

for line in lignes:
    for characters in line:
        output += characters + ' '
    output += ' moyenne : ' + str(moyennes[compteur]) + '\n'
    compteur += 1


fichier_output = open(file=dir_output, mode='w')
fichier_output.write(output)
fichier_output.close()

print(output)
