import random as rd

#Programme1

liste = [1,45,13,58,40,12]
liste.sort()
print (liste[-2])

#Programme2


def valid_ligne (sudoku,ligne_n):
    ligne = sudoku[ligne_n-1]
    if ligne[0] != ligne[1] and ligne[0] != ligne[2] and ligne[0] != ligne[3] :
        return(True)
    else:
        return(False)


sudoku_liste = [[],[],[],[]]
for i in range(4):
    for y in range(4):
        sudoku_liste[i].append(rd.randint(1,4))
print(sudoku_liste)
print(valid_ligne(sudoku_liste,))