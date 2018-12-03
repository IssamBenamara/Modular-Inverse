# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 13:54:50 2018

@author: ubuntu
"""

import projet2
import projet
import random

""" test de primalité de fermat """
def test_fermat( N, k = 4 ):
    """
    input:
    
    N = entier, à tester si premier
    k = nombre d'entiers a ( selon le petit theorème de fermat )
    ------------
    output:
    
    probably_prime = True si probablement premier, False si composé
    """
    
    if ( N == 2 ):
        return True
        
    if ( N & 1 == 0 ):
        return False
    while( k > N - 1 ):
        k -= 1
    a_list = random.sample(range(1, N), k )

    for a in a_list:
        if( projet.my_gcd( a, N ) == 1 ):
            if ( projet.my_expo_mod(a, N - 1, N) != 1 ):
                return False
    return True
    
""" generer un nombre composé inférieur à N """
def gen_compose( N ):
    """
    input:
    N = borne sup
    ----------
    output:
    a*b = nombre composé inférieur à N
    """
    a = N
    b = 2
    while ( a*b > N ):
        a = random.randint(1,int(N/2))
        b = random.randint(1,int(N/2))
    return a*b
    

""" test de la fonction test_fermat """
#
#carmichaels = projet2.gen_carmichael_comb( 5000 )
#print("test avec des carmichael")
#for car in carmichaels:
#    print(str(car[0])+" : "+str(test_fermat(car[0])))
#
#composes = [ gen_compose( 5000 ) for i in range(5) ]
#print("test avec des composés")
#for comp in composes:
#    print(str(comp)+" : "+str(test_fermat(comp)))
#    
#aleatoirs = [ random.randint(1, 5000) for i in range(5) ]
#print("test avec des aléatoires")
#for al in aleatoirs:
#    print(str(al)+" : "+str(test_fermat(al)))

""" Estimation experimental du taux d'erreur """
def proba_erreur_fermat( N, nbrTests, distinct = False ):
    """
    input:
    N = borne sup des entiers à tester
    nbrTests = nombre d'entiers à tester
    distinct = si True, le tirage aléatoire des nombres à tester sera sans remise ( aucun nombre n'est testé plus d'une fois )
    ---------
    output:
    probabilité d'erreur ( prédire un premier qui n'est pas premier )
    """
    count = 0
    if( distinct ):
        echantillon = random.sample(range(1,N+1),nbrTests)
        for i in echantillon:
            if( test_fermat(i) ): # si le test de fermat dit "probablement premier"
                if (  not projet2.first_test(i) ): # on test alors la primalité du nombre
                    count += 1
    else:
        echantillon = range(nbrTests)
        for i in echantillon:
            n = random.randint(1,N+1)
            if( test_fermat(n) ):
                if (  not projet2.first_test(n) ):
                    count += 1
    return count*1.0/nbrTests
    
""" test de proba_erreur_fermat """
#print(proba_erreur_fermat(100000, 100000, distinct = True))

