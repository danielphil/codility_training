def solution(A, B, C):
    planks = len(A)
    nailed = [False] * planks
    still_to_nail = planks
    
    # iterate through all the nails
    for nail_index in range(len(C)):
        nail = C[nail_index]
        for i in range(planks):
            if not nailed[i] and A[i] <= nail <= B[i]:
                nailed[i] = True
                still_to_nail -= 1

        if still_to_nail == 0:
            # all planks nailed
            return nail_index + 1 
        
    return -1