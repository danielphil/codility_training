A = [2, 3, 7, 5, 1, 3, 9]
k = 4
m = 6

P = [0] * (len(A) + 1)
for i in range(1, len(A) + 1):
    P[i] = A[i - 1] + P[i - 1]
print(P)

best_start = 0
best_end = 0
max_sum = 0

start_pos = max(0, k - m)
for pos in range(start_pos, k + 1):
    moves = k - pos
    remaining = m - moves
    end_pos = max(k, min(pos + remaining, len(A) - 1))
    current_sum = P[end_pos + 1] - P[pos]
    if (current_sum > max_sum):
        max_sum = current_sum
        best_start = pos
        best_end = end_pos

print("start: {0} end: {1} sum: {2}".format(best_start, best_end, max_sum))