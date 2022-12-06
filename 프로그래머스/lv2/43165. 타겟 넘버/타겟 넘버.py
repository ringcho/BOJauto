def solution(numbers, target):
    N = len(numbers)
    used = [0] * N
    check = []
    answer = 0

    def dfs(s, temp):
        if s == N:
            t = [x for x in used]
            if temp == target and (used not in check):
                check.append(t)
                nonlocal answer
                answer += 1
            return
        if temp + sum(numbers[s:])*2 < target:
            return
        
        if not used[s]:
            used[s] = 1
            dfs(s + 1, temp + numbers[s] * 2)
            used[s] = 0
            dfs(s + 1, temp)

    dfs(0, -sum(numbers))

    return answer