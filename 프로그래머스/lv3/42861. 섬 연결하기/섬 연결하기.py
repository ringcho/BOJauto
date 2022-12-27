def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    parent = [x for x in range(n)]
    answer = 0
    def find_parent(p, x):
        if p[x] != x:
            p[x] = find_parent(p, p[x])
        return p[x]
    def union(p, a, b):
        a = find_parent(p, a)
        b = find_parent(p, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    for s,e,value in costs:
        if find_parent(parent, s) != find_parent(parent, e):
            union(parent, s, e)
            answer += value
    return answer