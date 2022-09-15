def postorder(n):
    if n:
        postorder(branch_l[n])
        postorder(branch_r[n])
        if stack:
            if tree[n] in keys:
                num2 = stack.pop()
                num1 = stack.pop()
                if tree[n] == '+':
                    stack.append(num1+num2)
                elif tree[n] == '-':
                    stack.append(num1-num2)
                elif tree[n] == '*':
                    stack.append(num1*num2)
                elif tree[n] == '/':
                    stack.append(num1/num2)
            else:
                stack.append(tree[n])
        else:
            stack.append(tree[n])
for tc in range(1,11):
    N = int(input())
    tree = [0]*(N+1)
    branch_l = [0]*(N+1)
    branch_r = [0]*(N+1)
    keys = ['+', '-', '/', '*']
    for _ in range(N):
        node_info = list(input().split())
        if node_info[1] in keys:
            p, key, ch1, ch2 = int(node_info[0]), node_info[1], int(node_info[2]), int(node_info[3])
            tree[p] = key
            branch_l[p] = ch1
            branch_r[p] = ch2
        else:
            p, key = int(node_info[0]), int(node_info[1])
            tree[p] = key
    stack = []
    postorder(1)
    print(f'#{tc} {int(stack[-1])}')
