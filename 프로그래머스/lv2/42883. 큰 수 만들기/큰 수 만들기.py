def solution(number, k):
    cnt = 0
    stack = []
    idx = 0
    for i,x in enumerate(number):
        if cnt == k:
            stack.append(x)
            continue
            
        if not stack:
            stack.append(x)
            
        else:
            while stack and stack[-1] < x:
                stack.pop()
                cnt += 1
                if cnt == k:
                    idx = i
                    break
            stack.append(x)
    while cnt < k:
        stack.pop()
        cnt += 1
    answer = ''.join(stack)
    return answer