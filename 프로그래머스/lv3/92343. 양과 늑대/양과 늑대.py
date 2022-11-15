def solution(info, edges):
    visited = [0]*len(info)
    visited[0] = 1
    answer = []
    def find_sheep(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return
        for edge in edges:
            p, c = map(int, edge)
            if visited[p] and not visited[c]:
                visited[c] = 1
                if info[c] == 1:
                    wolf += 1
                else:
                    sheep += 1
                find_sheep(sheep, wolf)
                if info[c] == 1:
                    wolf -= 1
                else:
                    sheep -= 1
                visited[c] = 0
    find_sheep(1,0)
    return max(answer)