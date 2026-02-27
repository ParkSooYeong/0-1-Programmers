def solution(my_string, queries):
    my_list = list(my_string)
    
    for i in range(len(queries)):
        s = queries[i][0]
        e = queries[i][1]
        
        my_list[s:e+1] = my_list[s:e+1][::-1]
    
    answer = ''.join(my_list)
    return answer
