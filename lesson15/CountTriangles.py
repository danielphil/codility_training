def solution(A):
    count = 0
    for p in range(len(A)):
        for q in range(p + 1, len(A)):
            for r in range(q + 1, len(A)):
                total = A[p] + A[q] + A[r]
                hyp = max(A[p], A[q], A[r])
                sides = total - hyp
                if sides > hyp:
                    count += 1
    
    return count