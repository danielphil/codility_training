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
        
    leader_counts = [0] * len(A)
    leader_count = 0
    for i in range(len(A)):
        if A[i] == potential_leader:
            leader_count += 1
        leader_counts[i] = leader_count
    
    if leader_count > len(A) // 2:
        # found a leader!
        return potential_leader, leader_counts
    else:
        return -1, []
        
def solution(A):
    leader, leader_counts = find_leaders(A)
    if not leader_counts:
        return 0
        
    total_leaders = 0
    #print('Leader counts: {}'.format(leader_counts))
    
    # skip the last element- we still need a right hand side to find an equileader
    for i in range(len(A) - 1):
        left_leaders = leader_counts[i]
        right_leaders = leader_counts[-1] - left_leaders
        #print('left_leaders: {} right_leaders: {}'.format(left_leaders, right_leaders))
        
        left_elements = i + 1
        right_elements = len(A) - left_elements
        #print('left_elements: {} right_elements: {}'.format(left_elements, right_elements))
        
        left_required = left_elements // 2
        right_required = right_elements // 2
        #print('left_required: {} right_required: {}'.format(left_required, right_required))
        
        sufficient_leaders_on_left = left_leaders > left_required
        sufficient_leaders_on_right = right_leaders > right_required
        #print('Left: {} Right: {}'.format(sufficient_leaders_on_left, sufficient_leaders_on_right))
        
        if sufficient_leaders_on_left and sufficient_leaders_on_right:
            total_leaders += 1
    
    return total_leaders