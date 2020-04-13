def tiros(n,k):
    if k == 0:
        yield [0]*n
    elif k <= n:
        for comb in tiros(n-1, k-1):
            yield [1] + comb
        
        for comb in tiros(n-1,k):
            yield [0] + comb

def count(bolos,comb,d):
    resp = 0
    mask = [0]*len(bolos)
    for i in range(0,len(comb)):
        if comb[i] == 1:
            for j in range(i,min(i+d,len(comb))):
                if mask[j] != 1:
                    resp += bolos[j]
                    mask[j] = 1
    return resp

def fuerza_bruta(bolos,bolas,d):
    best = 0
    bolos = [0]*d + bolos + [0]
    for comb in tiros(len(bolos),bolas):
        c = count(bolos,comb,d)
        best = max(best,c)
    return best
