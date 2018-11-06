import unittest

def daniel_queue(A):
    current_people = 0
    min_people = 0

    for c in A:
        if c == 1:
            if current_people == 0:
                min_people += 1
            else:
                current_people -= 1
        else:
            current_people += 1
    
    return min_people

def codility_queue(A):
    n = len(A)
    size, result = 0, 0
    for i in xrange(n):
        if A[i] == 0:
            size += 1
        else:
            size -= 1
            result = max(result, -size)
    return result

class Test(unittest.TestCase):
    def test_simple(self):
        A = [1, 0, 0, 0, 1, 0, 0]
        self.assertEqual(daniel_queue(A), codility_queue(A))

    def test_complex(self):
        A = [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0]
        self.assertEqual(daniel_queue(A), codility_queue(A))

if __name__ == '__main__':
    unittest.main()