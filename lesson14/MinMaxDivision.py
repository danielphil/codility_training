def validate_blocks(K, A, max_sum):
    block_count = 1
    block_sum = 0
    for v in A:
        # add this value into the current block
        block_sum += v
        
        # does this new value make the sum of the block too large?
        if block_sum > max_sum:
            # start a new block
            block_count += 1
            block_sum = v
            
        # have we created too many blocks?
        if block_count > K:
            return False
    
    return True
            
def solution(K, M, A):
    # keep trying different min_sum possibilities until we find the smallest value that works
    lower_bound = max(A)
    upper_bound = sum(A)
    
    while lower_bound != upper_bound:
        max_sum = (lower_bound + upper_bound) // 2
        if validate_blocks(K, A, max_sum):
            upper_bound = max_sum
        else:
            lower_bound = max_sum + 1
            
    return lower_bound
    