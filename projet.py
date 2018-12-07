#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 11:03:58 2018

@author: Issam BENAMARA & Ismael BONNEAU
"""

import matplotlib.pyplot as plt
from random import randint
import big_o
from time import sleep
import sys
import time


def my_gcd( a, b ):
    """ 
    input :

    a = entier
    b = entier
    --------------
    output :

    pgcd(a,b)

    """
    
    while (b != 0):
        a,b=b,a%b
    return abs(a)

""" Test my_gcd"""
#print(my_gcd(11,-4))
    
def my_inverse( a, N ):
    """ 
    input :

    a = entier
    N = entier
    --------------
    output :

    b = inverse modulo N de a

    """
    N = abs(N)
    for b in range(N):
        if( (a*b)%N == 1 ):
            return b
    return 0
    """ 
    # retourner 0 pour calculer la complexité, causer une exception pour d'autres utilisation de la fonction
    raise ValueError( str(a) + " n'est pas inversible modulo " + str(N) )
    """
    
    
""" Test my_inverse """
#try:
#    print(my_inverse( 3, 7))
#except ValueError as err:
#    print(err.args)
#

    
""" Juste pour l'utiliser dans complexity, car ça requiert une fonction a une seule entrée  """
def my_inverse_tuple( tupleAN ):
    #print(tupleAN)
    return my_inverse( tupleAN[0], tupleAN[1])

def my_gcd_tuple( tupleAB ):
    #print(tupleAB)
    return my_gcd( tupleAB[0], tupleAB[1])

#print(my_inverse_tuple((3,7)))

def complexityMyInverse( NbTests, intRange ):
    """
    input:
    
    NbTests = nombre de tests à effectuer avec la fonction my_inverse_tuple
    intRange = défini une borne maximum à ne pas dépasser pour la generation de données en entrée de la fonction ( generation d'un entier entre 0 et intRange )
    --------
    output:
    
    complexité expérimentale de la fonction my_inverse_tuple ( de préférence donner de grandes valeurs NbTests et intRange pour être précis )
    """
    data_generator = lambda n: big_o.datagen.tuple(0, intRange)
    
    best, others = big_o.big_o(my_inverse_tuple, data_generator, n_repeats=NbTests)
    
    print(best)
 
def complexityMyGCD( NbTests, intRange ):
    """
    input:
    
    NbTests = nombre de tests à effectuer avec la fonction my_gcd_tuple
    intRange = défini une borne maximum à ne pas dépasser pour la generation de données en entrée de la fonction ( generation d'un entier entre 0 et intRange )
    --------
    output:
    
    complexité expérimentale de la fonction my_gcd_tuple ( de préférence donner de grandes valeurs NbTests et intRange pour être précis )
    """
    data_generator = lambda n: big_o.datagen.tuple(0, intRange)
    
    best, others = big_o.big_o(my_gcd_tuple, data_generator, n_repeats=NbTests)
    

    print(best)
    
""" test generation de data """
#tes = lambda n: big_o.datagen.tuples(10, 0, 100)
#print(tes(1))

""" test complexity """
#complexityMyInverse(1000, 1000000)  """ exponential """
#complexityMyGCD(100000, 1000000)  """ linear / logarithmic at best """

""" Courbe my_inverse par rapport à N """
def graphMyInverse( intRange, verbose = False ):
    """
    input :
    
    intRange = défini une borne maximum à ne pas dépasser pour la generation de données en entrée de la fonction ( generation d'un entier entre 0 et intRange )
    --------
    output:
    
    courbe du temps d'execution de my_inverse en fonction de N ( avec le a généré aléatoirement à chaque fois, N incrémenté de 10 à chaque fois )
    """
    sys.stdout.write('\n')
    measures = []
    for i in range(0, intRange, 10):
        a , N = randint(0, intRange), i
        start = time.time()
        my_inverse( a, N )
        end = time.time()
        measures.append(end-start)
        
        if(verbose):
            """ progress bar """
            sys.stdout.write('\r')
            # the exact output you're looking for:
            sys.stdout.write("[%-20s] %d%%" % ('=='*(int(10*(i+1)/intRange)+1), int(100*(i/intRange))))
            sys.stdout.flush()
            sleep(0.25)
            """ progress bar end """
        
    if(verbose):
        sys.stdout.write('\n')
    plt.plot(range(0, intRange, 10), measures)  # on utilise la fonction sinus de Numpy
    plt.ylabel('Execution Time')
    plt.xlabel("N")
    plt.show()

""" Courbe my_cgd par rapport à b """
def graphMyGCD( intRange, verbose = False ):
    """
    input :
    
    intRange = défini une borne maximum à ne pas dépasser pour la generation de données en entrée de la fonction ( generation d'un entier entre 0 et intRange )
    --------
    output:
    
    courbe du temps d'execution de my_inverse en fonction de N ( avec le a généré aléatoirement à chaque fois, N incrémenté de 10 à chaque fois )
    """
    sys.stdout.write('\n')
    measures = []
    for i in range(0, intRange, 10):
        a , b = randint(0, intRange), i
        start = time.time()
        my_gcd( a, b )
        end = time.time()
        measures.append(end-start)
        
        if(verbose):
            """ progress bar """
            sys.stdout.write('\r')
            # the exact output you're looking for:
            sys.stdout.write("[%-20s] %d%%" % ('=='*(int(10*(i+1)/intRange)+1), int(100*(i/intRange))))
            sys.stdout.flush()
            sleep(0.25)
            """ progress bar end """
        
    if(verbose):
        ys.stdout.write('\n')
    plt.plot(range(0, intRange, 10), measures)  # on utilise la fonction sinus de Numpy
    plt.ylabel('Execution Time')
    plt.xlabel("N")
    plt.show()
    
""" affichage courbes de complexité """    
#graphMyInverse(100)
#graphMyGCD(1000)



""" Exponentiation discrète binaire """

def my_expo_mod( g, n, N ):
    """
    input:
    g = entier
    n = entier
    N = entier
    --------------
    output:
    
    h = (g ** n) % N   ===       ( g puissance n ) mod N 
    """
    h = 1
    
    #construction de la liste en binaire de n ( son ordre est deja du plus grand exposant au plus petit )
    a_List = list("{0:b}".format(n)) # ATTENTION liste de char et non pas d'entiers

    for ai in a_List: 
        h = (h*h)%N
        if( ai == '1' ): # comparaison avec un char, car la a_Liste contient des char
            h = (h*g)%N
            
    return h
    
    
""" ecriture alternative de l'exponentiation modulaire """
def power(x, y, p) : 
    res = 1     # Initialize result 
    # Update x if it is more 
    # than or equal to p 
    x = x % p  
  
    while (y > 0) : 
          
        # If y is odd, multiply 
        # x with result 
        if ((y & 1) == 1) : 
            res = (res * x) % p 
  
        # y must be even now 
        y = y >> 1      # y = y/2 
        x = (x * x) % p 
          
    """ retourne (x ** y) mod p """
    return res 
       
      
     
""" test de l'exponentiation modulaire avec les différentes implémentations, et l'implémentation python """
#g,n,N = 2,7,15
#print(my_expo_mod(g,n,N))
#print(power(g,n,N))
#print(pow(g,n,N))
