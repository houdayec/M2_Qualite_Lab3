# coding: utf-8
def getNext(password):

    pwd = list(password) #1 récupération du mot de passe et transformation en list de charactères pour les analyser
    found = False
    lengthPassword=len(pwd)
    print("Longueur du mot de passe {}".format(lengthPassword))

    while not found:
        if lengthPassword > 1:
            for i in range(lengthPassword-1, 0, -1):
                print("Index {}".format(i))
                if pwd[i] < 'z': 
                    pwd[i] = chr(ord(pwd[i])+1) #2 remplacement du charactèretrouvé par le charactère suivant dans l'alphabet (+1)
                if i == 0:
                    found = True
        else:
            if pwd[lengthPassword-1] < 'z': 
                pwd[lengthPassword-1] = chr(ord(pwd[lengthPassword-1])+1) #2 remplacement du charactère z trouvé par le charactère suivant dans l'alphabet (+1) -> a
                found = True
            else:
                found = True

    return ''.join(pwd) #3 retour du mot de passe transformé

    
# TESTS
print(getNext('b'))
print(getNext('bz'))
print(getNext('cd'))