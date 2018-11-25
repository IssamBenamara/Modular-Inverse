# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 09:28:35 2018

@author: ubuntu
"""

import math

""" test naif de primalité sur un entier N """
def first_test( N ):
    """
    input:
    N = entier
    -----------
    output:
    True si N est premier, False sinon
    """
    
    for k in range(1,int(math.sqrt(N))+1):
        if( k % N == 0 ):
            return False
    return True
    

""" compléxité de first_test theoriquement O( racine ( N ))