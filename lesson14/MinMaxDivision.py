from collections import namedtuple
# failing input (10000, 100, [42])
Range = namedtuple('Range', ['begin', 'end'])

def partial_sums(A):
    sums = [0] * (len(A) + 1)
    for i in range(len(A)):
        sums[i + 1] = A[i] + sums[i]
        
    return sums

def range_total(sums, r):
    return sums[r.end + 1] - sums[r.begin]

def split_range(sums, r):
    # choose split point in centre
    # calculate total for each half
    # store max value
    # split left and right ranges again
    begin = r.begin
    end = r.end
    best_split = (begin + end) // 2
    max_total = range_total(sums, r)
    split = best_split
    
    while True:
        left_range = Range(r.begin, split)
        right_range = Range(split + 1, r.end)
        #print('left: {} right: {}'.format(left_range, right_range))
        left_total = range_total(sums, left_range)
        right_total = range_total(sums, right_range)
        #print('left_total: {} right_total: {}'.format(left_total, right_total))
        #print('max_total: {}'.format(max_total))
        
        if left_total == right_total:
            return Range(r.begin, best_split), Range(best_split + 1, r.end)

        new_max = max(left_total, right_total)
        if new_max >= max_total:
            # our new split was worse or no better than what we had already
            # so give up
            return Range(r.begin, best_split), Range(best_split + 1, r.end)
        else:
            max_total = new_max
            best_split = split
            
        if left_total > right_total:
            # move the split on the left side
            end = split
        else:
            # move the split on the right side
            begin = split
    
        split = (begin + end) // 2        

def solution(K, M, A):
    
    sums = partial_sums(A)

    ranges = [Range(0, len(A) - 1)]

    while len(ranges) <= K:
        max_range = 0
        max_range_index = 0
        for i in range(len(ranges)):
            s = range_total(sums, ranges[i])
            if s > max_range:
                max_range_index = i
                max_range = s
        
        a, b = split_range(sums, ranges[max_range_index])
        ranges[max_range_index] = a
        ranges.append(b)
        
    return max_range