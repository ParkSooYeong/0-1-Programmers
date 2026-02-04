def solution(numLog):
    control = []
    
    for i in range(len(numLog) - 1):
        if numLog[i+1] == None:
            break
        elif numLog[i] + 1 == numLog[i+1]:
            control.append('w')
        elif numLog[i] - 1 == numLog[i+1]:
            control.append('s')
        elif numLog[i] + 10 == numLog[i+1]:
            control.append('d')
        elif numLog[i] - 10 == numLog[i+1]:
            control.append('a')

    answer = ''.join(control)
    return answer
