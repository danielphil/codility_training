// Pretty much based on https://rafal.io/posts/codility-max-double-slice-sum.html
// :(

def solution(A):
    left_sum = [0] * len(A)
    right_sum = [0] * len(A)
    
    for i in range(1, len(A) - 1):
        left_sum[i] = max(0, left_sum[i - 1] + A[i])

    for i in range(len(A) - 2, 0, -1):
        right_sum[i] = max(0, right_sum[i + 1] + A[i])
    
    max_sum = 0
    for i in range(1, len(A) - 1):
        max_sum = max(max_sum, left_sum[i - 1] + right_sum[i + 1])
        
    return max_sum