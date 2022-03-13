def to_base10 (input,old_base):
    output = 0
    puissance = len(str(input))-1
    for nb in str(input):
        output += int(nb)*(old_base**puissance)
        puissance -= 1
    print('\n',input,'en base',old_base,'correspond à',output,'en base 10','\n')
    return(output)

def base10_to (input,new_base):
    liste = []
    number = input
    output = str()
    while input != 0:
        liste.append(input % new_base)
        input = input // new_base
    liste.reverse()
    for i in liste:
        output += str(i)
    output = int(output)
    print ('\n',number,'correspond à',output,'en base',new_base,'\n')
    return(output)

request_func = input('\nChoisir entre encrypt (1) et decrypt (2):      ')
if request_func == '1':
    print('\nok\n\nEncrypt consiste à transformer un nb de base 10 vers la base choisie\n')
    entry = int(input('     Quel est le nombre ?    '))
    base = int(input('     Quel est la base choisie ?    '))
    base10_to(entry,base)
elif request_func == '2':
    print('\nok\n\nDecrypt consiste à transformer un nb de base inconnue vers la base 10\n')
    entry = int(input('     Quel est le nombre ?    '))
    base = int(input('     Quel est la base choisie ?    '))
    to_base10(entry,base)
else:
    exit()