def solution(num_list):
    
    multiple = 1
    
    for i in range(len(num_list)):
        multiple *= num_list[i]
        
        if multiple < (sum(num_list) * sum(num_list)):
            answer = 1
        else:
            answer = 0

    return answer
