def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for i in range(2, int(total**0.5)+1):
        if total % i == 0:
            w = total//i
            h = i
            if brown == ((w-1) + (h-1))*2:
                return([w,h])
    return answer