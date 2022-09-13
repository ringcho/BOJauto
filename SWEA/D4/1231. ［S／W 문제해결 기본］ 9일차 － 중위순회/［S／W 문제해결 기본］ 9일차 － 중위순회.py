def inorder(n):
    global visited
    if n:
        inorder(branch_l[n])
        visited += nodes[n]
        inorder(branch_r[n])



for tc in range(1,11):
    V = int(input())
    nodes = [0]*(V+1)
    branch_l = [0]*(V+1)
    branch_r = [0]*(V+1)
    for _ in range(V):
        adj_info = list(map(str, input().split()))
        if len(adj_info) == 4:
            p, bl, br = int(adj_info[0]), int(adj_info[2]), int(adj_info[3])
            nodes[p] = adj_info[1]
            branch_l[p] = bl
            branch_r[p] = br
        elif len(adj_info) == 3:
            p, bl = int(adj_info[0]), int(adj_info[2])
            nodes[p] = adj_info[1]
            branch_l[p] = bl
        else:
            p = int(adj_info[0])
            nodes[p] = adj_info[1]

    visited = ''
    inorder(1)
    print(f'#{tc} {visited}')