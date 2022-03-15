import rotate_matrix as rm


matrice = []
for i in range(7):
    matrice.append([])
    for j in range(7):
        matrice[i].append(0)
matrice[0][0] = 1
for i in matrice:
    print(i)
print('\n')
matrice = rm.anti_clockwise(matrice)
for i in matrice:
    print(i)
