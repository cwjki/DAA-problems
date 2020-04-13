from math import factorial

def combinaciones(n,k):
    return factorial(n)/(factorial(n-k)*factorial(k))

def acum_sum(elems):
    sum = []
    sum.append((elems[0],0))
    for i in range(1,len(elems)):
        sum.append((sum[i-1][0] + elems[i],i))
    return sum

def init_solution(elemens):
    temp_sum = sorted(acum_sum(elemens))
    sum = []
    index = []
    item = temp_sum.pop()
    sum.append(item[0])
    index.append([item[1]])
    while len(temp_sum) > 0:
        item = temp_sum.pop()
        if item[0] == sum[len(sum)-1]:
            index[len(index)-1].append(item[1])
        else:
            sum.append(item[0])
            index.append([item[1]])
    return sum,index

def binary_search(elems, P, left, rigth):
    while left < rigth:
        mid = int((left + rigth)/2)
        if P(mid):
            rigth = mid
        else:
            left = mid + 1
    return left

def lower_bound(elems, k):
    def P(x):
        return elems[x] >= k
    return binary_search(elems, P, 0, len(elems)-1)

def count_interv(index1,index2):
    count = 0
    a = 0
    b = 0
    if index1[0] == index2[0]:
        count += ( len(index1) * (len(index1)-1)) / 2 
    else:
        while b != len(index2) and a != len(index1):
            if index1[a] > index2[b]:
                count += len(index2) - b
                a += 1
            else:
                b += 1
    return count

def count_men(elems,k):
    if len(elems) == 0:
        return 0
    pos = lower_bound(elems,k)
    if elems[pos] < k:
        return pos + 1
    return pos

def get_array(length,minValue,maxValue):
    if length == 0:
        yield []
    else:
        for i in range(minValue,maxValue + 1):
            for item in get_array(length-1,minValue,maxValue):
                yield [i] + item