from random import *
from Fuerza_Bruta import subintervalos_FB
from Solution_2 import solution_2
from Auxiliares import get_array

def tester(sol1,sol2):
    count = 0
    for elems in get_array(10,-3,3):
        for i in range(-15,16):
            s1 = sol1(elems,i,i,i)
            s2 = sol2(elems,i,i,i)
            assert s1 == s2
            count += 1
            print(count)

def tester(sol1,sol2):
    count = 0
    rdm = Random()
    while True:
        items = []
        for _ in range(0,rdm.randint(1,10000)):
            items.append(rdm.randint(-1000,1000))
            k = rdm.randint(-2000,2000)
            a = rdm.randint(-2000,2000)
            b = rdm.randint(-2000,2000)
            a,b = min(a,b),max(a,b)
            s1 = sol1(items,k,a,b)
            s2 = sol2(items,k,a,b)
            assert s1 == s2
            count += 1
            print(count)


tester(subintervalos_FB,solution_2)