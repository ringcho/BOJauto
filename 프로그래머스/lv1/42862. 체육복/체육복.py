def solution(n, lost, reserve):
    answer = n - len(lost)
    get = []
    no_lost = []
    lost.sort()
    reserve.sort()
    
    for number in lost:
        if number in reserve:
            answer += 1
            no_lost.append(number)
            
    for number in no_lost:
        lost.remove(number)
        reserve.remove(number)
    
    for number in lost:
        if number-1 in reserve and number not in get:
            answer += 1
            get.append(number)
            reserve.remove(number-1)
        elif number + 1 in reserve and number not in get:
            answer += 1
            get.append(number)
            reserve.remove(number+1)
            
    return answer