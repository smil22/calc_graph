# -*- coding: utf-8 -*-

from lib import *
print("*** AFFICHEUR DE COURBE DE FONCTION (ax² + bx + c) ***")
n = int(input("Combien de courbes: "))
x = styler_graphe(-4,4)
for i in range(n):
    print("Fonction", i+1, ":")
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    tracer_f(a,b,c,x)
afficher_f()
