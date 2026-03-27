def solution(arr):
    answer = []
    buffer = []
    
    for i in range(len(arr)):
        if arr[i] == 2:
            buffer.append(i)
    
    if len(buffer) == 0:
        answer.append(-1)
    else:
        answer = arr[buffer[0]:buffer[-1] + 1]
    
    return answer
