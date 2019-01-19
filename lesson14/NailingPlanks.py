def validate(A, B, C, nails_to_use):
    planks = len(A)
    sorted_nails = sorted(C[:nails_to_use])

    for i in range(planks):
        nailed = False
        for nail in sorted_nails:
            if A[i] <= nail <= B[i]:
                nailed = True
                break

        if not nailed:
            return False

    return True

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
