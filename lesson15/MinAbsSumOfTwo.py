import random

def brute_force(A):
    result = 2000000000
    for i in range(len(A)):
        for j in range(i, len(A)):
            result = min(result, abs(A[i] + A[j]))

    return result

def optimised(A):
    # remove duplicated elements and sort in ascending order
    A = sorted(set(A))
    if len(A) < 2:
        return abs(A[0] + A[0])

    overall_min_sum = 2000000000
    r_index = len(A) - 1
    for l_index in range(len(A)):
        r_index = min(r_index, len(A) - 1)
        l = A[l_index]
        
        # check the value paired with itself
        min_abs_sum = abs(l + l)
        overall_min_sum = min(min_abs_sum, overall_min_sum)

        if l_index == len(A) - 1:
            # no right element to compare with
            return overall_min_sum

        if l >= 0:
            # value is positive, so smallest sum is abs(l + l)
            # choosing any more values will only make the sum larger
            if min_abs_sum > overall_min_sum:
                # we can't make the sum any smaller
                return overall_min_sum
            else:
                overall_min_sum = min_abs_sum
        else: # l < 0
            # try to minimise abs(l + r) to see if we can get the sum smaller
            # try to find the ideal value of r
            required = abs(l)

            r = A[r_index]
            best_sum = abs(l + r)
            if r > required:
                increment = -1
                end_index = l_index
            elif r < required:
                increment = 1
                end_index = len(A)
            else: # r == required
                # min sum will be 0 because l + r == 0
                return 0

            while r_index + increment != end_index:
                new_sum = abs(l + A[r_index + increment])
                if new_sum < best_sum:
                    best_sum = new_sum
                    r_index += increment
                else:
                    break         
            
            overall_min_sum = min(best_sum, overall_min_sum)

    return overall_min_sum

if __name__ == "__main__":
    for i in range(30):
        A = [random.randint(-20, 20) for v in range(21)]
        correct = brute_force(A)
        new = optimised(A)
        if correct != new:
            print('correct: {} new: {} A: {}'.format(correct, new, A))