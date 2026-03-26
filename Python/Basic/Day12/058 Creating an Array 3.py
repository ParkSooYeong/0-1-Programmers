def solution(arr, intervals):
    answer = []
    
    for i in range(len(intervals)):
        a = intervals[i][0]
        b = intervals[i][1]
        
        answer += arr[a:b+1]
    
    return answer
