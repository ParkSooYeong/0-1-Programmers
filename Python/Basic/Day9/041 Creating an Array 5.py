def solution(intStrs, k, s, l):
    answer = []
    
    for i in range(len(intStrs)):
        intlist = intStrs[i][s:s+l]
        
        if int(intlist) > k:
            answer.append(int(intlist))
    
    return answer
