import math
import numpy as np
import random
import matplotlib.pyplot as plt
from scipy.stats import norm
from matplotlib.ticker import FuncFormatter

def one_choice(m, n):

    vector = np.zeros(m, dtype=int)
    
    for _ in range(n):
        posicion = random.randint(0, m - 1)
        vector[posicion] += 1  

    return vector

def d_choice(m, n, d):

    vector = np.zeros(m, dtype=int)
    
    for _ in range(n):
        posicion = random.randint(0, m - 1)
        for _ in range(d):
            posicionaux = random.randint(0, m - 1)
            if(vector[posicionaux] < vector[posicion]):
                posicion = posicionaux 
        vector[posicion] += 1 

    return vector

def one_plus_beta_choice(m, n, beta, b):

    vector = np.zeros(m, dtype=int)
        
    prob = 1-beta
    for _ in range(int(n//b)):
        aux = np.zeros(m, dtype=int)
        for _ in range(b):    
            posicion = random.randint(0, m - 1)
            if random.random() < prob:
                posicionaux = random.randint(0, m - 1)
                if(vector[posicionaux] < vector[posicion]):
                    posicion = posicionaux 
            aux[posicion] += 1 
        vector += aux
        

    return vector
