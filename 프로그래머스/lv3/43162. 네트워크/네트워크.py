def solution(n, computers):
    visited = [0]*n
    answer = 0
    def dfs(i):    
        if visited[i]:
            return
        else:
            for j in range(n):
                if not i == j and computers[i][j]:
                    visited[i] = 1
                    dfs(j)
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    print(visited)
    return answer