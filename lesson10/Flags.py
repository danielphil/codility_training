def place_flags(peaks, flags):
    if len(peaks) == 0:
        return False
    
    if len(peaks) == 1:
        return flags == 1
        
    placed_flags = 1
    s = peaks[0]
    i = 1
    while i < len(peaks):
        if peaks[i] - s >= flags:
            placed_flags += 1
            s = peaks[i]
            
            if placed_flags >= flags:
                return True
        i += 1
    
    return False
    
def solution(A):
    peaks = []
    for p in range(1, len(A) - 1):
        if A[p - 1] < A[p] > A[p + 1]:
            peaks.append(p)
    
    for flags in range(len(peaks), 0, -1):
        if place_flags(peaks, flags):
            return flags
            
    return 0
