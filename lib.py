"""utilise les paramètres reçus pour tracer et afficher une courbe"""

import matplotlib.pyplot as plt
import numpy as np

def styler_graphe(xmin,xmax):
    """installe le décor pour tracer les fonctions"""
    x = np.linspace(xmin, xmax, 100)
    fig = plt.figure(figsize = (10,5))
    plt.grid()
    plt.xlabel("x")
    plt.ylabel("f(x)", rotation=0)
    return x

def tracer_f(a,b,c,x):
    """trace la courbe"""
    y = a*x**2 + b*x + c
    plt.plot(x,y, label = f"({a})x²+({b})x+({c})")

def afficher_f():
    """affiche la courbe"""
    if plt.legend() != None:
        plt.legend()
    plt.show()
