def solution(N):
    a = 1
    p = 2 * (1 + N)
    while a * a <= N:
        b = None
        if a * a == N:
            b = a
        elif N % a == 0:
            b = N // a

        if b:
            p = min(2 * (a + b), p)
                    
        #print("a: {} b: {}".format(a, b))   

        a += 1
        
    return p