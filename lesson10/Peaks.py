def count_peaks(peaks, factor, total):
    for group in range(0, total // factor):
        start = group * factor
        end = group * factor + factor
        #print('start: {} end: {} group: {} factor: {} total: {}'.format(start, end, group, factor, total))
        for i in range(start, end):
            if i in peaks:
                # this group has a peak, so we can move on
                #print('found peak')
                break
        else:
            # no peak found
            #print('no peak found')
            return 0
    
    return total // factor
    
def solution(A):
    count = len(A)
    peaks = set()
    max_peaks = 0
    for i in range(1, count - 1):
        v = A[i]
        if A[i - 1] < v and v > A[i + 1]:
            # found peak
            peaks.add(i)
    
    i = 1
    # find factors
    while i <= count:
        if i * i == count:
            max_peaks = max(max_peaks, count_peaks(peaks, i, count))
            max_peaks = max(max_peaks, count_peaks(peaks, i * i, count))
        elif count % i == 0:
            # found a factor
            max_peaks = max(max_peaks, count_peaks(peaks, i, count))
            max_peaks = max(max_peaks, count_peaks(peaks, count // i, count))

        i += 1
    
    return max_peaks