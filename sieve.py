import unittest
from functools import reduce

# based on Codility's notes on Sieve of Eratosthenes
def sieve(n):
    # create a list where prime numbers are marked with True, and non-prime 
    # with False
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False

    i = 2

    # only need to perform this up to sqrt(i)
    while (i * i <= n):
        # if this value is still marked as prime
        if (sieve[i]):
            # mark i ^ 2 as not prime
            k = i * i
            while (k <= n):
                sieve[k] = False
                # mark subsequent multiples as prime
                k += i
        i += 1
    
    # just the primes!
    return [p for p in range(n + 1) if sieve[p] == True]

def get_factors(n):
    factors = [0] * (n + 1)
    i = 2

    while i * i <= n:
        if factors[i] == 0:
            k = i * i
            while k <= n:
                if factors[k] == 0:
                    factors[k] = i
                k += i
        
        i += 1
    
    return factors

def factorise(n):
    factors = get_factors(n)
    result = []

    i = n
    while factors[i] > 0:
        result.append(factors[i])
        i //= factors[i]
    result.append(i)

    return result

def product(iterable):
    return reduce(lambda x, y: x * y, iterable, 1)

class Test(unittest.TestCase):
    def test_sieve(self):
        primes = sieve(29)
        expected_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        self.assertEqual(primes, expected_primes)

    def test_get_factors(self):
        factors = get_factors(20)
        expected_factors = [0, 0, 0, 0, 2, 0, 2, 0, 2, 3, 2, 0, 2, 0, 2, 3, 2, 0, 2, 0, 2]
        self.assertEqual(factors, expected_factors)

    def test_factorise(self):
        factors = factorise(2)
        expected_factors = [2, 2, 5]
        self.assertEqual(factors, expected_factors)
        self.assertEqual(product(expected_factors), 20)

if __name__ == "__main__":
    unittest.main()