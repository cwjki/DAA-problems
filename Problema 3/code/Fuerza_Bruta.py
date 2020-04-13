from Auxiliares import combinaciones

def subintervalos_FB(elems,k,a = 0,b = 0):
    if len(elems) == 1:
        count_k = 0
        count_ab = 0
        if elems[0] == k:
            count_k += 1
        if a <= elems[0] <= b:
            count_ab += 1
        return count_k,count_ab
    else:
        count_k = 0
        count_a = 0
        count_b = 0
        for i in range(0,len(elems)):
            sum = 0
            for j in range(i,len(elems)):
                sum += elems[j]
                if sum == k:
                    count_k += 1
                if sum < a:
                    count_a += 1
                if sum > b:
                    count_b += 1
        return count_k, combinaciones(len(elems),2) - count_a - count_b