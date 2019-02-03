def solution(A):
    N = len(A)
    rolls = [1, 2, 3, 4, 5, 6]
    sums = [A[0]] + [None] * (N - 1)

    for i in range(1, N):
        for j in rolls:
            if i - j >= 0:
                current_sum = sums[i - j] + A[i]
                if sums[i] is None:
                    sums[i] = current_sum
                else:
                    sums[i] = max(sums[i], sums[i - j] + A[i])
            else:
                break
                
    return sums[N - 1]