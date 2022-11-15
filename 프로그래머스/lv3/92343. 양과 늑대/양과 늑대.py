def solution(info, edges):
    visited = [0]*len(info)
    visited[0] = 1
    answer = []
    def find_sheep(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return
        for i in range(len(edges)):
            p, c = map(int, edges[i])
            child_is_wolf = info[c]
            if visited[p] and not visited[c]:
                visited[c] = 1
                if child_is_wolf == 1:
                    wolf += 1
                else:
                    sheep += 1
                find_sheep(sheep, wolf)
                if child_is_wolf == 1:
                    wolf -= 1
                else:
                    sheep -= 1
                visited[c] = 0
    find_sheep(1,0)
    return max(answer)