def solution(A, B):
    set_end = None
    set_count = 0
    
    for (start, end) in zip(A, B):
        if set_end is None or start > set_end:
            # found a new set that doesn't overlap
            set_count += 1
            set_end = end
            
    return set_count