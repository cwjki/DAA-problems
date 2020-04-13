def acum_sum(elems):
    resp = [0] * len(elems)
    resp[0] = elems[0]
    for i in range(1,len(elems)):
        resp[i] = resp[i-1] + elems[i]
    return resp

def max_solapan(dp,i,j,ancho,suma):
    best = dp[i-1][max(0,j-1)]-(suma[max(0,j-1)]-suma[max(0,j-ancho)])
    for k in range(max(0,j-ancho+1),j):
        best = max(best, dp[i-1][k]-(suma[k]-suma[max(0,j-ancho)]))
    return best

def solution_1(bolos,tiros,ancho):
    bolos = [0] + bolos + [0] * ancho
    suma = acum_sum(bolos)
    dp = []
    max_dp = []
    for i in range(0,tiros + 1):
        dp.append([0] * len(bolos))
        max_dp.append([0] * len(bolos))
    max_value = 0
    dp[1][0] = 0    
    max_dp[1][0] = 0
    for i in range(1,len(bolos)):
        dp[1][i] = suma[i] - suma[max(0,i-ancho)]
        max_dp[1][i] = max(dp[1][i],max_dp[1][i-1])

    for i in range(2,tiros + 1):
        for j in range(0,len(bolos)):
            max_s = max_solapan(dp,i,j,ancho,suma)
            max_ns = max_dp[i-1][max(0,j-ancho)]
            dp[i][j] = dp[1][j] + max(max_s,max_ns)
            max_dp[i][j] = max(dp[i][j],max_dp[i][max(0,j-1)])
    return max(dp[tiros])
