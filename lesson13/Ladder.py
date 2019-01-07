def solution(A, B):
    result = []
    
    for a, b in zip(A, B):
        count = 0
        p = 2 ** b
        
        for i in range(1, a // 2 + 1):
            count += a - i
            count %= p
            
        if a % 2 == 1:
            count += 1
            count %= p
            
        result.append(count)
        
    return result