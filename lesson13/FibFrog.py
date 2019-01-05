def generate_fib():
    # skip the first two elements.
    # No point in duplicating 1 or jumping 0
    fib = [1, 2]
    while True:
        next = fib[-1] + fib[-2]
        if next > 100000:
            return fib
            
        fib.append(next)
        
    return fib

def solution(A):
    # tests:
    # [1, 1, 0, 0, 0]
    # [0, 0, 0]
    # []
    # [1]
    
    # if there's either no river, or just one section of river,
    # we can always clear it in one jump
    if len(A) < 2:
        return 1
        
    fib = generate_fib()
    
    # add the end bank to the river
    river = A + [1]
    
    # build an array of minimum jumps to reach each position on
    # the river
    
    # initialize the min_jumps list from our starting position
    min_jumps = [0] * len(river)
    for jump in fib:
        pos = jump - 1
        if pos < len(river) and river[pos] == 1:
            min_jumps[pos] = 1
    
    # the last element of min_jumps holds the number of jumps required
    # to reach the bank
    if min_jumps[-1] == 1:
        # We were able to jump to the bank already!
        return 1
    
    for i in range(len(river) - 1):
        if min_jumps[i] == 0:
            # this element can't be jumped to
            continue
        
        # hop from this location to see where we can jump to
        for jump in fib:
            j = i + jump
            if j >= len(river):
                # jumped past the end of the river
                continue
            
            if river[j] == 0:
                # nothing to jump to here
                continue
            
            new_jumps = min_jumps[i] + 1
            # update min_jumps at j if min_jumps was either 0 at
            # that position, or we've found a smaller number of jumps
            if min_jumps[j] == 0:
                min_jumps[j] = new_jumps
            elif min_jumps[j] > new_jumps:
                min_jumps[j] = new_jumps
    
    if min_jumps[-1] == 0:
        # we were never able to reach the bank
        return -1
    else:
        # final element contains the minimum number of jumps to reach the bank
        return min_jumps[-1]