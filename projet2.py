# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 09:28:35 2018

@author: ubuntu
"""

import math
import sys
from time import sleep
import projet

""" test naif de primalité sur un entier N """
def first_test( N ):
    """ compléxité de first_test theoriquement O( racine ( N )) """
    
    """
    input:
    N = entier
    -----------
    output:
    True si N est premier, False sinon
    """
    if( N < 4 ):
        if ( N > 1 ):
            return True
    for k in range(2,int(math.sqrt(N))+1):
        if( N%k == 0 ):
            return False
    return True
    
""" comptage des nombres premiers inférieurs à N """
def count_primal_under( N ):
    """
    input:
    N = entier
    -----------
    output:
    _sum = combien de nombres entiers sont inférieurs ou égale à N
    """
    
    _sum = 0
    for i in range(N+1):
        
        """ progress bar """
        sys.stdout.write('\r')
        # the exact output you're looking for:
        sys.stdout.write("[%-20s] %d%%" % ('=='*(int(10*(i+1)/(N+1))+1), int(100*(i/(N+1)))))
        sys.stdout.flush()
        sleep(0.25)
        """ progress bar end """
        
        if( first_test(i) ):
            _sum +=1
    
    sys.stdout.write('\n')
    print("Prime numbers count under " + str(N) +" : " + str(_sum) )
    return _sum

""" test de la fonction comptage """
#count_primal_under(100)

""" verifier si un nombre est un Carmichael """

""" 

!!!!

CETTE FONCTION N'EST PAS CORRECTE CERTAINS NOMBRES SONT CONSIDERE COMME CORRECTE ALORS QUE NON, COMME 563 IL FAUT LA CORRIGER 
!
!!!


"""
def isCarmichaelNumber( N ) : 
    """
    input:
    N = entier
    -----------
    output:
    True si N est Carmichael, False sinon
    
    -------------
    power(b, n-1) MOD n = 1, 
    for all b ranging from 1 to n such that b and 
    n are relatively prime, i.e, gcd(b, n) = 1 
    
    On vérifie en meme temps si c'est un nombre premier
    
    https://www.geeksforgeeks.org/carmichael-numbers/
    """
    prime = True
    b = 2
    while ( b < N ): 
          
        # If "b" is relatively prime to n 
        if ( projet.my_gcd(b, N) == 1) : 
  
            # And pow(b, n-1)% n is not 1, 
            # return false. 
            if ( projet.my_expo_mod(b, N - 1, N) != 1 ): 
                return False
        else:
            prime = False
        b = b + 1
    return not prime

""" test Carmichael """
#print(isCarmichaelNumber(561))

""" generer des entiers Carmichael inférieurs  ou égal à N """
def gen_carmichael( N ):
    """
    input:
    N = entier
    -----------
    output:
    cars = List d'entiers Carmichael inférieurs ou égal à N
    """
    
    cars = []
    for i in range(560,N+1):
        """ On commence à tester à partir de 560 vu que l'on sait deja que le premier nombre carmichael est 561 """ 
        
        """ progress bar """
        sys.stdout.write('\r')
        # the exact output you're looking for:
        sys.stdout.write("[%-20s] %d%%" % ('=='*(int(10*(i+1)/(N+1))+1), int(100*(i/(N+1)))))
        sys.stdout.flush()
        sleep(0.25)
        """ progress bar end """
        
        if( isCarmichaelNumber(i) ):
            cars.append(i)
    
    sys.stdout.write('\n')
    return cars

""" Test génération de Carmichael : ATTENTION prend du temps quand même ! """    
#print(gen_carmichael(3000))


def facteurpremier(n):
    """int->liste[int]
       renvoi la liste des facteurs premierd de n."""

    s=2
    L=[]
    x=int(n**0.5)+1
    if first_test(n)==True:   
        return n
    else:
        for s in range (2,x):
            if n%s==0:
                if first_test(s)==True:
                    L.append(s)
    return L

from random import randint

def primal_under( N ):
    """
    input:
    N = entier
    -----------
    output:
    _sum = combien de nombres entiers sont inférieurs ou égale à N
    """
    
    _sum = []
    for i in range(N+1):
        
        """ progress bar """
        sys.stdout.write('\r')
        # the exact output you're looking for:
        sys.stdout.write("[%-20s] %d%%" % ('=='*(int(10*(i+1)/(N+1))+1), int(100*(i/(N+1)))))
        sys.stdout.flush()
        sleep(0.25)
        """ progress bar end """
        
        if( first_test(i) ):
            _sum.append(i)
    
    sys.stdout.write('\n')
    return _sum

""" Generation de Carmichael à 3 facteurs premiers """
import itertools
from random import shuffle

def gen_carmichael_3fp( N ):
    liste = primal_under( int(math.sqrt(N)) )
    if( liste == [] ):
        return -1
    perm = list(itertools.combinations(liste, 3))
    shuffle(perm)
    x = -1
    for p in perm:
        x = p[0]*p[1]*p[2]
        if( isCarmichaelNumber(x) ):
            return x
    return -1

import big_o
def complexity_isCarmichaelNumber( NbTests, intRange ):
    """
    input:
    
    NbTests = nombre de tests à effectuer avec la fonction my_inverse_tuple
    intRange = défini une borne maximum à ne pas dépasser pour la generation de données en entrée de la fonction ( generation d'un entier entre 0 et intRange )
    --------
    output:
    
    complexité expérimentale de la fonction my_inverse_tuple ( de préférence donner de grandes valeurs NbTests et intRange pour être précis )
    """
    data_generator = lambda n: randint(0,intRange)
    
    best, others = big_o.big_o(isCarmichaelNumber, data_generator, n_repeats=NbTests)
    
    print(best)
    
print(gen_carmichael_3fp(570))