def solution(my_string, n):
    behind = len(my_string) - n
    answer = ''.join(my_string[behind:])
    return answer
