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

def generate_sums(semiprimes):
    partial_sums = [0] * (len(semiprimes) + 1)
    for i in range(1, len(semiprimes)):
        partial_sums[i] = semiprimes[i] + partial_sums[i - 1]
    return partial_sums

def solution(N, P, Q):
    # perhaps partial sums for performance?
    factors = smallest_factors(N)
    semiprimes = [0] * (N + 1)
    start = min(P)
    end = max(Q)
    for i in range(start, end + 1):
        # if the number is not prime, find the list of divisors
        if factors[i] != 0:
            divisor = factors[i]
            # we can only find one more prime factor for the number to be classed
            # as semiprime
            if factors[i // divisor] == 0:
                semiprimes[i] = 1

    #print([i for i in range(len(semiprimes)) if semiprimes[i]])
    
    sums = generate_sums(semiprimes)
    
    results = []
    for i in range(len(P)):
        start = P[i]
        end = Q[i]
        results.append(sums[end] - sums[start - 1])

    return results