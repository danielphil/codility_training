def solution(K, A):
    current_length = 0
    long_ropes = 0
    
    for length in A:
        current_length += length
        if current_length >= K:
            long_ropes += 1
            current_length = 0
            
    return long_ropes