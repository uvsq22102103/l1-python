def hamming(bits):
    '''Prend 7 bits en entrée et rend 4 bits de données
    (C'est un code de correction d'erreur de Hamming).
    L'inverse est également possible !'''
    if len(bits) == 7 :
        #definition des bits de vérification et de données
        k1, k2, k4 = int(bits[-1]), int(bits[-2]), int(bits[-4])
        m1, m2, m3, m4 = int(bits[-3]), int(bits[-5]), int(bits[-6]), int(bits[-7])
        parité_1, parité_2, parité_4 = (m1+m2+m4)%2, (m1+m3+m4)%2, (m2+m3+m4)%2
        if parité_1 != k1 and parité_2 != k2 and parité_4 != k4:
            #erreur m4
            if m4 == 0:
                m4 = 1
            else:
                m4 = 0
        elif parité_1 != k1 and parité_2 != k2 and parité_4 == k4:
            #erreur m1
            if m1 == 0:
                m1 = 1
            else:
                m1 = 0
        elif parité_1 != k1 and parité_2 == k2 and parité_4 != k4:
            #erreur m2
            if m2 == 0:
                m2 = 1
            else:
                m2 = 0
        elif parité_1 == k1 and parité_2 != k2 and parité_4 != k4:
            #erreur m3
            if m3 == 0:
                m3 = 1
            else:
                m3 = 0
        return(str(m4)+str(m3)+str(m2)+str(m1))
    elif len(bits) == 4:
        pass
    else:
        print('Input non valide')

print(hamming('1001101'))