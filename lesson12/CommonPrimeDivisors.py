# ended up getting an explanation for the solution for this one
# from http://codility-lessons.blogspot.com/2015/03/lesson-10-commonprimedivisors.html

def gcd(A, B):
    if A % B == 0:
        return B
    else:
         return gcd(B, A % B)

def check_value(v, g):
    remaining = v / g
    while (g % remaining != 0):
        new_gcd = gcd(remaining, g)
        if new_gcd == 1:
            return False
    
        remaining //= new_gcd
    
    return True
         
def solution(A, B):
    Z = len(A)
    count = 0
    
    for a, b in zip(A, B):
        g = gcd(a, b)

        # check a and b contain all the same prime factors
        if check_value(a, g) and check_value(b, g):
            count += 1

    return count