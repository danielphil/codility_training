def solution(A):
    max_a = max(A)
    divisors = {}
    counts = {}
    for val in A:
        divisors[val] = set([1, val])
        if val in counts:
            counts[val] += 1
        else:
            counts[val] = 1
    
    i = 2
    # no divisor can be greater than sqrt(max_a)
    while i * i <= max_a:
        current = i
        # iterate through all multiples of i, adding to a set if one exists
        while current <= max_a:
            if current in divisors:
                divisors[current].add(i)
                divisors[current].add(current // i)
            current += i
        i += 1
    
    results = [0] * len(A)
    for i in range(len(A)):
        remaining = len(A)
        for d in divisors[A[i]]:
            if d in counts:
                remaining -= counts[d]
        results[i] = remaining
        
    return results