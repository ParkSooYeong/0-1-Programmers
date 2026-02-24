def solution(a, b, c, d):
    answer = 0
    dice = [a, b, c, d]
    
    # 개수 세기
    # 딕셔너리를 쓰는 이유 = key : value 형태로 특정 key가 몇의 value를 갖는지 파악할 수 있음.
    count = {}
    for num in dice:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    # 경우 나누기
    # 4개 다 같은 경우 , count의 길이가 1일 때(딕셔너리에 원소가 하나일 때)
    if len(count) == 1:
        p = dice[0]
        answer = 1111 * p
    
    # 두 종류의 숫자가 있는 경우
    elif len(count) == 2:
        values = list(count.values()) # 1개+3개인지 2개+2개인지 판별
        
        # 1개+3개인 경우
        if 3 in values:
            for key in count:
                if count[key] == 3:
                    p = key
                else:
                    q = key
            answer = (10 * p + q) * (10 * p + q)
        
        # 2개+2개인 경우
        else:
            keys = list(count.keys())
            p = keys[0]
            q = keys[1]
            answer = (p + q) * abs(p - q)
    
    # 2개+1개+1개인 경우
    elif len(count) == 3:
        singles = []
        
        # 2개는 볼 필요 없고 이 이외에 1개+1개만 보면 됨
        for key in count:
            if count[key] == 1:
                singles.append(key)
        answer = singles[0] * singles[1]
        
    # 4개 전부 다른 경우
    else:
        answer = min(dice)

    return answer
