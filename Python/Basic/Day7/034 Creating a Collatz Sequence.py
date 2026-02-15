def solution(n):
    answer = []
    x = n
    
    answer.append(x)
    
    while True:
        if x == 1:
            break
            
        if x % 2 == 0:
            answer.append(x // 2)
            x = x // 2
        elif x % 2 == 1:
            answer.append(3 * x + 1)
            x = 3 * x + 1
        
    return answer
