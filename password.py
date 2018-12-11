# coding: utf-8
def getNext(password):
        """
        Série de tests exprimés en doctest
        >>> getNext('b')
        'c'
        >>> getNext('bz')
        'cb'
        >>> getNext('cd')
        'ce'
        """

        pwd = list(password) #1
        found = False
        i=len(pwd)-1

        while not found:
        if pwd[i] < 'z': 
        5
        pwd[i] = chr(ord(pwd[i])+1) #2
        found = True
        else:
        i = i-1

        return ''.join(pwd) #3

        # A l’aide de cette partie du code, si vous exécutez ce fichier, les tests doctests seront exécutés en même temps.
        # Pour stopper l’exécution des tests, commentez les deux lignes ci-dessous.
        # Pour lancer manuellement les tests, commentez aussi les lignes, et utilisez "python -m doctest pass.py" au clavier.
        if __name__ == "__main__":
        import doctest
        doctest.testmod()