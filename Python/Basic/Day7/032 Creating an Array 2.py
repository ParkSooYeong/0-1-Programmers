def solution(l, r):
    answer = []
    
    for num in range(l, r + 1):
        is_valid = True
        
        for i in str(num):
            if i != '0' and i != '5':
                is_valid = False
                break
                
        if is_valid:
            answer.append(num)
    
    if len(answer) == 0:
        answer.append(-1)
    
    return answer
