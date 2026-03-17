def solution(my_string):
    answer = []
    
    for i in range(52):
        answer.append(0)
    
    for i in my_string:
        if i.isupper():
            answer[ord(i)-65] += 1
        elif i.islower():
            answer[ord(i)-71] += 1
    
    return answer
