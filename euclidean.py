import unittest

def gcd_subtraction(a, b):
    if a == b:
        return a
    
    if a > b:
        return gcd_subtraction(a - b, b)
    else:
        return gcd_subtraction(a, b - a)

def gcd_division(a, b):
    if a % b == 0:
        return b
    else:
        return gcd_division(b, a % b)

def gcd_binary(a, b, scaling):
    if a == b:
        return scaling * a
    elif a % 2 == 0 and b % 2 == 0:
        return gcd_binary(a // 2, b // 2, 2 * scaling)
    elif a % 2 == 0:
        return gcd_binary(a // 2, b, scaling)
    elif b % 2 == 0:
        return gcd_binary(a, b // 2, scaling)
    elif a > b:
        return gcd_binary(a - b, b, scaling)
    else:
        return gcd_binary(a, b - a, scaling)

def lcm(a, b):
    return (a * b) / (gcd_division(a, b))

class Test(unittest.TestCase):
    test_params = [
        (54, 24, 6),
        (24, 54, 6),
        (6, 6, 6)
    ]

    def test_subtraction(self):
        for a, b, result in self.test_params:
            self.assertEqual(gcd_subtraction(a, b), result)

    def test_division(self):
        for a, b, result in self.test_params:
            self.assertEqual(gcd_division(a, b), result)

    def test_binary(self):
        for a, b, result in self.test_params:
            self.assertEqual(gcd_binary(a, b, 1), result)

    def test_lcm(self):
        self.assertEqual(lcm(9, 12), 36)

if __name__ == "__main__":
    unittest.main()