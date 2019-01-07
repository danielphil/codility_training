def solution(A, B):
    max_a = max(A)
    max_b = max(B)

    fib = [0] * (max_a + 2)
    fib[1] = 1
    
    for i in range(2, max_a + 2):
        fib[i] = (fib[i - 1] + fib[i - 2]) % (2 ** max_b)
    
    result = [0] * len(A)
    for i in range(len(A)):
        result[i] = fib[A[i] + 1] % (2 ** B[i])
        
    return result