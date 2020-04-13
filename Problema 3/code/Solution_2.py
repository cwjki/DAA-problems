from Auxiliares import *
from AVL import *

def igual_k(elems,k):
    elems = [0] + elems
    A,A_index = init_solution(elems)
    count_k = 0
    i = 0
    j = 0
    while i < len(A) and j < len(A):
        r = A[i] - A[j]
        if r > k:
            i += 1
        elif r < k:
            j +=1
        else:
            count_k += count_interv(A_index[i],A_index[j])
            i += 1
            j += 1
    return count_k

def menores_que(elems,a):
    count = 0
    elems = [0] + elems
    A,A_Index = init_solution(elems)
    I = None
    i = 0
    j = 0
    while i < len(A) and j < len(A):
        r = A[i] - A[j]
        if r < a:
            for item in A_Index[j]:
                I = insert(I,item)
            j += 1
        else:
            for t in range(0,len(A_Index[i])):
                count += countSmallers(I,A_Index[i][t])
            i += 1
    while i < len(A_Index):
        for t in range(0,len(A_Index[i])):
            count += countSmallers(I,A_Index[i][t])
        i += 1
    return count

def mayores_que(elems,b):
    count = 0
    elems = [0] + elems
    A,A_Index = init_solution(elems)
    I = None
    for i in range(0,len(elems)):
        I = insert(I,i)
    i = 0
    j = 0
    while i < len(A) and j < len(A):
        r = A[i] - A[j]
        if r > b:
            for t in range(0,len(A_Index[i])):
                count += countSmallers(I,A_Index[i][t])
            i += 1
        else:
            for t in range(0,len(A_Index[j])):
                I = deleteNode(I,A_Index[j][t])
            j += 1
    while i < len(A_Index):
        for t in range(0,len(A_Index[i])):
            count += countSmallers(I,A_Index[i][t])
        i += 1
    return count

def menor_mayor_que(elems,a,b):
    count_a = menores_que(elems,a)
    count_b = mayores_que(elems,b)
    if len(elems) == 1:
        return max(0,1 - count_a - count_b)
    return combinaciones(len(elems),2) - count_a - count_b

def solution_2(elems,k,a,b):
    return igual_k(elems,k),menor_mayor_que(elems,a,b)