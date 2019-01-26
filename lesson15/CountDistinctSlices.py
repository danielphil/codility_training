# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# (100000, [1, 1])
# (100000, [100000, 10000])

from random import randint

def good_solution(M, A):
    slices = 0
    for start in range(len(A)):
        values = set([A[start]])
        slices += 1
        #print('({}, {})'.format(start, start))
        if slices > 1000000000:
            return 1000000000
        
        for end in range(start + 1, len(A)):
            if A[end] in values:
                # repeated element
                break
            
            slices += 1
            #print('({}, {})'.format(start, end))
            if slices > 1000000000:
                return 1000000000
            values.add(A[end])
            
    return slices

def calculate_slices(A, range_start, range_end):
    # https://en.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_⋯
    n = range_end - range_start + 1
    return (n * (n + 1)) // 2
    
def solution(M, A):
    slices = 0
    
    start = 0
    end = 0
    value_present = [False] * (M + 1)
    
    end = 0
    while end < len(A):
        value = A[end]
        if not value_present[value]:
            # this is a value we haven't seen before, so record that
            # we've seen it and move on
            value_present[value] = True
            end += 1
        else:
            # keep moving the start forward until we've found the repeating
            # value or we've caught up to the end
            while start <= end - 1 and value_present[value]:
                slices += end - start
                value_present[A[start]] = False
                start += 1
            
    # Count the remaining slices for the final segment of the array
    slices += calculate_slices(A, start, len(A) - 1)
    
    return min(slices, 1000000000)

def find_failure_cases():
    M = 10
    A = [3, 4, 5, 5, 2]
    for i in range(10):
        A = [randint(1, M) for p in range(1000)]
        good_result = good_solution(M, A)
        new_result = solution(M, A)
        if new_result != good_result:
            print('Failed! Good: {} New {} A: {}'.format(good_result, new_result, A))

if __name__ == "__main__":
    #find_failure_cases()

    M = 10
    A = [3, 3, 10, 6, 5, 3, 5, 8, 3, 1]
    good_result = good_solution(M, A)
    new_result = solution(M, A)

    print('Good result: {} New result: {}'.format(good_result, new_result))

