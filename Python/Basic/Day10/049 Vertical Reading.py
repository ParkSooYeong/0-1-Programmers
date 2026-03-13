def solution(my_string, m, c):
    answer = []
    
    for i in range(len(my_string)):
        if i % m == 0:
            answer.append(my_string[(i-1)+c])
            
    answer = ''.join(answer)

    return answer
