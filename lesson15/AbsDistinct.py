def solution(A):
    negative_pos = -1
    positive_pos = len(A)
    
    # find the point where negative values end and positive (or zero)
    # values start
    for i in range(len(A)):
        if A[i] >= 0:
            positive_pos = i
            negative_pos = i - 1
            break
    else:
        negative_pos = len(A) - 1

    distinct_count = 0
    while negative_pos != -1 or positive_pos != len(A):
        move_negative = False
        move_positive = False
        if negative_pos != -1 and positive_pos != len(A):
            a = abs(A[negative_pos])
            b = abs(A[positive_pos])
            
            if a < b:
                move_negative = True
            elif b < a:
                move_positive = True
            else:
                move_negative = True
                move_positive = True
        else:
            if negative_pos == -1:
                move_positive = True
            elif positive_pos == len(A):
                move_negative = True
                
        if move_positive:
            v = A[positive_pos]
            while positive_pos != len(A) and A[positive_pos] == v:
                positive_pos += 1
                
        if move_negative:
            v = A[negative_pos]
            while negative_pos != -1 and A[negative_pos] == v:
                negative_pos -= 1
                
        distinct_count += 1

    return distinct_count