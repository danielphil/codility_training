# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def build_prime_factors(n):
    prime_factors = [0] * (n + 1)
    i = 2
    
    while i * i <= n:
        if prime_factors[i] == 0:
            k = i * i
            while k <= n:
                if prime_factors[k] == 0:
                    prime_factors[k] = i
                k += i
        i += 1
        
    return prime_factors

def get_factors(v, prime_factors):
    # all values can be divided by 1
    factors = [1]
    if v > 1:
        # we can be divided by ourselves
        factors += [v]
        
        # this is a prime number, so no further divisors
        if prime_factors[v] == 0:
            return factors
        
        primes = { prime_factors[v] }
        new_primes = [prime_factors[v]]
        while new_primes:
            #print('Primes: {} New Primes: {}'.format(primes, new_primes))
            current_prime = new_primes.pop()
            c = v
            while c % current_prime == 0 and c != current_prime:
                c = c // current_prime
                factors += [c]
                fac = prime_factors[c]
                if fac > 0 and fac not in primes:
                    if c > 1:
                        primes.add(fac)
                        new_primes.append(fac)
                        factors += [fac]
                elif fac == 0 and c not in primes:
                    # found a prime number
                    if c > 1:
                        primes.add(c)
                        new_primes.append(c)
                    break

    return factors
    
def solution(A):
    max_value = len(A) * 2 + 1
    val_count = [0] * max_value
    
    for v in A:
        val_count[v] += 1
    
    result = [0] * len(A)
    prime_factors = build_prime_factors(max_value)
    for i in range(len(A)):
        factors = get_factors(A[i], prime_factors)
        remaining_elements = len(A)
        for f in factors:
            remaining_elements -= val_count[f]
        result[i] = remaining_elements
    
    return result    
    # check for length 0 and 1
    
    #print(get_factors(27, build_prime_factors(30)))