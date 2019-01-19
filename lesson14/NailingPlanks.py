def validate(A, B, C, nails_to_use):
    planks = len(A)
    nailed = [False] * planks
    still_to_nail = planks

    
    for nail_index in range(nails_to_use):
        nail = C[nail_index]
        for i in range(planks):
            if not nailed[i] and A[i] <= nail <= B[i]:
                nailed[i] = True
                still_to_nail -= 1

        if still_to_nail == 0:
            # all planks nailed
            return True
    
    return False

def solution(A, B, C):
    # binary search through all the nails
    lower_bound = 1
    upper_bound = len(C)
    
    while lower_bound != upper_bound:
        mid = (lower_bound + upper_bound) // 2
        if validate(A, B, C, mid):
            upper_bound = mid
        else:
            lower_bound = mid + 1

    if validate(A, B, C, lower_bound):
        return lower_bound
    else:
        return -1
