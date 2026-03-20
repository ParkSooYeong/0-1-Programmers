def solution(my_string, indices):
    list_string = list(my_string)
    
    for i in sorted(indices, reverse = True):
        list_string.pop(i)
    
    answer = ''.join(list_string)
    
    return answer
