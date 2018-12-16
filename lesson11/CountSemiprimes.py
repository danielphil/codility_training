def smallest_factors(N):
    # generate array of smallest prime divisors up to N
    factors = [0] * (N + 1)
    
    i = 2
    while i * i <= N:
        if factors[i] == 0:
            k = i * i
            while k <= N:
                if factors[k] == 0:
                    factors[k] = i
                k += i
        i += 1
    
    return factors
    
def solution(N, P, Q):
    # perhaps partial sums for performance?
    factors = smallest_factors(N)
    semiprimes = [False] * (N + 1)
    start = min(P)
    end = max(Q)
    for i in range(start, end + 1):
        # if the number is not prime, find the list of divisors
        if factors[i] != 0:
            divisor = factors[i]
            val = i
            current_factors = []
            while factors[val] != 0:
                val = val // divisor
                current_factors += [val]
            current_factors += [divisor]
            if (len(current_factors) == 2):
                semiprimes[i] = True
    
    #print([i for i in range(len(semiprimes)) if semiprimes[i]])
    
    results = []
    for i in range(len(P)):
        start = P[i]
        end = Q[i]
        count = 0
        for j in range(start, end + 1):
            if semiprimes[j]:
                count += 1
        results.append(count)
        
    return results