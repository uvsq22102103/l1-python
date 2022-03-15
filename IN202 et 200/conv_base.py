def conversionBase (number,base=2):
    if number == 0:
        return (0)
    else:
        liste = list()
        while number != 0 :
            liste.append(number%base)
            number = number // base
        liste.reverse()
        return (liste)

def afficheBase(liste):
    for v in liste:
        print(v,end="")

def conversionDecimal(liste,b=2):
    res = 0
    puissance = len(liste)-1
    for v in liste :
        res += v*b**puissance
        puissance -= 1
    return(res)

def ajout_bits(nombre,longueur=8):
    to_add = longueur - len(nombre)
    for boucle in range(to_add):
        nombre.insert(0,0)
    return(nombre)

def additionBases(liste1,liste2,bases):
    if len(liste1) > len(liste2):
        ajout_bits(liste2,len(liste1))
    elif len(liste1) < len(liste2):
        ajout_bits(liste1,len(liste2))
    else:
        pass
    pass

print('\n')
test = conversionBase(115)
print(test)
ajout_bits(test)
print(test)
print('\n')