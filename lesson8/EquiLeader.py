def find_leaders(A):
    potential_leader = A[0]
    count = 1
    for i in range(1, len(A)):
        if count == 0:
            potential_leader = A[i]
            count += 1
        elif A[i] == potential_leader:
            count += 1
        else:
            count -= 1
    
    if count == 0:
        return -1, []
        
    leader_positions = []
    for i in range(len(A)):
        if A[i] == potential_leader:
            leader_positions.append(i)
    
    if len(leader_positions) > len(A) // 2:
        # found a leader!
        return potential_leader, leader_positions
    else:
        return -1, []
        
def solution(A):
    print(find_leaders(A))
    
    pass