def solution(A):
    max_ending_here = A[0]
    max_so_far = A[0]
    
    for element in A[1:]:
        max_ending_here = max(element, max_ending_here + element)
        max_so_far = max(max_so_far, max_ending_here)
        
    return max_so_far