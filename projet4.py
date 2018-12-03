# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 16:20:12 2018

@author: ubuntu
"""

import projet
import random
import projet2
import sys

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


def test_miller_rabin( N, T = 7 ):
    
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
    
for i in range(10000):
    N = random.randint(1,5000)
    reality = projet2.first_test(N)
    mine = test_miller_rabin(N)
    first = is_prime(N)
    second = miller_rabin(N)
    if(not reality):
        assert(not mine)
    if(not first):
        assert(not mine)
    if(not second):
        assert(not mine)
    #print("N : "+str(N)+"\t prime : "+str(reality)+"\t mine : "+str(mine)+"\t first : "+str(first)+"\t second : "+str(second))