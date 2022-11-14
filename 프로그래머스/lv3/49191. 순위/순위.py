def solution(n, results):
    answer = 0
    winner = [[] for _ in range(n+1)]
    loser = [[] for _ in range(n+1)]
    for result in results:
        a, b = result[0], result[1]
        loser[a].append(b)
        winner[b].append(a)
    
    for x in loser:
        for y in x:
            for l in loser[y]:
                if l not in x:
                    x.append(l)
    for x in winner:
        for y in x:
            for w in winner[y]:
                if w not in x:
                    x.append(w)
    for i in range(n+1):
        if len(winner[i]) + len(loser[i]) == n-1:
            answer += 1
    return answer