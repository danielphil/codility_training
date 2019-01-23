# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(M, A):
    slices = 0
    for start in range(len(A)):
        values = set([A[start]])
        slices += 1
        if slices > 1000000000:
            return 1000000000
        
        for end in range(start + 1, len(A)):
            if A[end] in values:
                # repeated element
                break
            
            slices += 1
            if slices > 1000000000:
                return 1000000000
            values.add(A[end])
            
    return slices
