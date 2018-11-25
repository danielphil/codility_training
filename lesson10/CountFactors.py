def solution(N):
    i = 1
    factors = 0
    #factor_list = []
    while i * i <= N:
        if i * i == N:
            # only count sqtr(N) once
            #factor_list.append(i)
            factors += 1
        elif N % i == 0:
            # count i and N/i as factors
            factors += 2
            #factor_list += [i, N // i]
            
        i += 1

    #factor_list.sort()
    #print(factor_list)
    return factors