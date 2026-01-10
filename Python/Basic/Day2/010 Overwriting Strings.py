def solution(my_string, overwrite_string, s):
    my_list = list(my_string)

    for i in range(len(overwrite_string)):
        my_list[i + s] = overwrite_string[i]

    answer = "".join(my_list)
    return answer
