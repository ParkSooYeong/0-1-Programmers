def solution(num_list):
    odd_list = []
    even_list = []
    answer = 0
    
    for i in range(len(num_list)):
        if num_list[i] % 2 == 1:
            odd_list.append(num_list[i])
        else:
            even_list.append(num_list[i])
    
    odd = ''.join(map(str, odd_list))
    even = ''.join(map(str, even_list))
            
    answer = int(odd) + int(even)
    
    return answer
