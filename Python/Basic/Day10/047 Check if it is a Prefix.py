def solution(my_string, is_prefix):
    for i in range(len(my_string)):
        if my_string[:i] == is_prefix:
            answer = 1
            break
        else:
            answer = 0

    return answer
