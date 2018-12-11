import unittest
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

class Test(unittest.TestCase):
    def test_example(self):
        primes = sieve(29)
        expected_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        self.assertEqual(primes, expected_primes)


if __name__ == "__main__":
    unittest.main()