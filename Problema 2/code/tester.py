from auxiliares import get_array
from fuerza_bruta import fuerza_bruta
from solution_1 import solution_1

def tester(sol1,sol2,length,minV,maxV,d,bolas):
    count = 0
    for array in get_array(length,minV,maxV):
        s1 = sol1(array,bolas,d)
        s2 = sol2(array,bolas,d)
        if s1 != s2:
            print("----------------")
            print(array)
            print(s1)
            print(s2)
            print("----------------")
        else:
            count+=1
            print(count)

tester(fuerza_bruta,solution_1,8,-5,8,3,3)