def solution(arr, queries):
    answer = []
    
    for j in range(len(queries)):
        temp = []
        s = queries[j][0]
        e = queries[j][1]
        k = queries[j][2]
        
        for i in arr[s:e+1]:
            if i > k:
                temp.append(i)
        
        if len(temp) == 0:
            temp.append(-1)
        
        answer.append(min(temp))
        
    return answer
