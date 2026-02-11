def solution(arr, queries):
    for j in range(len(queries)):
        s = queries[j][0]
        e = queries[j][1]
        k = queries[j][2]
        
        for i in range(s, e + 1):
            if i % k == 0:
                arr[i] += 1
        
    return arr
