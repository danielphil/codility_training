import random

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

# test [10, 2, 5, 1, 8, 12] 

def new_solution(A):
    # need 3 elements to make this work
    if len(A) < 3:
        return 0

    # sort first
    count = 0
    A.sort()
    
    for p_index in range(len(A) - 2):
        # we can share r_index across iterations of q.
        # if A[p] + A[q] > A[r], then A[p] + A[q + 1] > A[r]
        r_index = p_index + 2
        for q_index in range(p_index + 1, len(A) - 1):
            p = A[p_index]
            q = A[q_index]
            # keep advancing r_index until we find a value that fails to satisfy p + q > r
            while r_index < len(A) - 1 and p + q > A[r_index + 1]:
                r_index += 1

            if p + q > A[r_index]:
                count += r_index - q_index

    return count

if __name__ == "__main__":
    for i in range(100):
        A = [random.randint(1,60) for p in range(20)]
        good = solution(A)
        new = new_solution(A)
        if good != new:
            print('Good: {} New: {} A: {}'.format(good, new, A))