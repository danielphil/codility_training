def solution(A):
    # no prices!
    if not A:
        return 0
    
    # only one price
    if len(A) == 1:
        return A[0]
        
    deltas = [0] * len(A)
    for i in range(1, len(A)):
        deltas[i] = A[i] - A[i - 1]
        
    max_ending_here = deltas[0]
    max_so_far = deltas[0]
    
    for p in deltas[1:]:
        max_ending_here = max(p, max_ending_here + p)
        max_so_far = max(max_so_far, max_ending_here)
        
    if max_so_far > 0:
        return max_so_far
    else:
        return 0
