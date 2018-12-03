# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 16:20:12 2018

@author: ubuntu
"""

import projet
import random
import projet2

def is_prime( n, k = 7 ):
   """use Rabin-Miller algorithm to return True (n is probably prime)
      or False (n is definitely composite)"""
   if n < 6:  # assuming n >= 0 in all cases... shortcut small cases here
      return [False, False, True, True, False, True][n]
   elif n & 1 == 0:  # should be faster than n % 2
      return False
   else:
      s, d = 0, n - 1
      while d & 1 == 0:
         s, d = s + 1, d >> 1
      # Use random.randint(2, n-2) for very large numbers
      for a in random.sample(range(2, min(n - 2, 1000000000)), min(n - 4, k)):
         x = pow(a, d, n)
         if x != 1 and x + 1 != n:
            for r in range(1, s):
               x = pow(x, 2, n)
               if x == 1:
                  return False  # composite for sure
               elif x == n - 1:
                  a = 0  # so we know loop didn't continue to end
                  break  # could be strong liar, try another a
            if a:
               return False  # composite if we reached end of this loop
      return True  # probably prime if reached end of outer loop
      
def miller_rabin(n, k=10):
	if n == 2 or n == 3:
		return True
	if not n & 1:
		return False

	def check(a, s, d, n):
		x = pow(a, d, n)
		if x == 1:
			return True
		for i in range(s - 1):
			if x == n - 1:
				return True
			x = pow(x, 2, n)
		return x == n - 1

	s = 0
	d = n - 1

	while d % 2 == 0:
		d >>= 1
		s += 1

	for i in range(k):
		a = random.randrange(2, n - 1)
		if not check(a, s, d, n):
			return False
	return True

""" Test de primalité de Miller-Rabin """
def test_miller_rabin( N, T = 7 ):
    """
    input:
    N = entier à tester si premier
    T = Nombre de de bases a à tester
    ----------------
    output:
    True si N est probablement premier, False si N est composé
    """
    if ( N < 6 ):  # assuming n >= 0 in all cases... shortcut small cases here
        return [False, False, True, True, False, True][N]
    elif ( N & 1 == 0 ):  # should be faster than n % 2
        return False
      
    h, m = 0, N -1
    while ( m & 1 == 0):
        h, m = h + 1, m >> 1
    #assert( N -1 == (2**h)*m)
    for a in random.sample( range( 2, N - 2 ), min( N - 4, T ) ):
        b = projet.my_expo_mod( a, m, N )
        if ( b != 1 and b != N - 1 ):
            for j in range(1, h):
                x = projet.my_expo_mod( b, 2, N )
                if (b != N - 1 and x == 1 ):
                    return False
                b = x
            if ( b != N - 1 ):
                return False
    return True

""" test de la fonction test_miller_rabin """
#
#carmichaels = projet2.gen_carmichael_comb( 5000 )
#print("test avec des carmichael")
#for car in carmichaels:
#    print(str(car[0])+" : "+str(test_miller_rabin(car[0])))
#
#composes = [ gen_compose( 5000 ) for i in range(5) ]
#print("test avec des composés")
#for comp in composes:
#    print(str(comp)+" : "+str(test_miller_rabin(comp)))
#    
#aleatoirs = [ random.randint(1, 5000) for i in range(5) ]
#print("test avec des aléatoires")
#for al in aleatoirs:
#    print(str(al)+" : "+str(test_miller_rabin(al)))

""" Estimation experimental du taux d'erreur """
def proba_erreur_miller_rabin( N, nbrTests, distinct = False ):
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
            if( test_miller_rabin(i) ): # si le test de fermat dit "probablement premier"
                if (  not projet2.first_test(i) ): # on test alors la primalité du nombre
                    count += 1
    else:
        echantillon = range(nbrTests)
        for i in echantillon:
            n = random.randint(1,N+1)
            if( test_miller_rabin(n) ):
                if (  not projet2.first_test(n) ):
                    count += 1
    return count*1.0/nbrTests
    
""" test de proba_erreur_fermat """
#print(proba_erreur_miller_rabin(10000000, 100000, distinct = False))
