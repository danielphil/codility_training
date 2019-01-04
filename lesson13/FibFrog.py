# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

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

def try_jump(pos, river, valid_jumps, jumps_so_far, best_so_far):
    if jumps_so_far > best_so_far:
        # don't bother continuing, we've already found a better route
        return -1
        
    best_jump = -1
    for potential_jump in reversed(valid_jumps):
        new_pos = pos + potential_jump
        if new_pos >= len(river) or river[new_pos] == 0:
            # jumped past the end of the river or into the water
            # try next jump size
            continue
        
        # valid jump!
        # if we've hit the bank, we're done
        if new_pos == len(river) - 1:
            return jumps_so_far + 1
        else:
            # make our next jump
            result = try_jump(new_pos, river, valid_jumps, jumps_so_far + 1, best_so_far)
            if result != -1:
                # we successfully jumped!
                if best_jump == -1:
                    best_jump = result
                else:
                    best_jump = min(result, best_jump)
        
    return best_jump
    
def solution(A):
    fib = generate_fib()
    
    # add the two banks to the river
    river = A + [1]
    
    # frog starts on the bank
    result = try_jump(-1, river, fib, 0, 100001)
    
    return result