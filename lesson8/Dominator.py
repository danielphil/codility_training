def solution(A):
    index = -1
    count = 0
    possible_leader = None
    for i in range(len(A)):
        element = A[i]
        if count == 0:
            possible_leader = element
            count = 1
            index = i
        elif element == possible_leader:
            count += 1
        else:
            count -= 1
            
    # couldn't find a leader
    if count == 0:
        return -1
    
    # verify leader
    count = 0
    for element in A:
        if element == possible_leader:
            count += 1
    
    required_leaders = len(A) // 2
    if count > required_leaders:
        # we have a leader
        return index
    else:
        return -1
