def solution(A, B):
    fib = [0] * 50002
    fib[1] = 1
    
    for i in range(2, 50002):
        fib[i] = fib[i - 1] + fib[i - 2]
    
    result = []
    for a, b in zip(A, B):
        result.append(fib[a + 1] % (2 ** b))
        
    return result
    