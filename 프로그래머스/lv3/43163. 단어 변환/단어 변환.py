def solution(begin, target, words):
    answer = len(words)
    n = len(target)
    visited = [begin]
    def dfs(temp, cnt):
        nonlocal answer
        if temp == target:
            answer = min(answer, cnt)
        for word in words:
            match = 0
            for i in range(n):
                if word[i] in temp[i]:
                    match += 1
            if match == n-1 and word not in visited:
                visited.append(word)
                dfs(word, cnt+1)
                visited.pop()
    dfs(begin, 0)
    if target not in words:
        return 0
    return answer