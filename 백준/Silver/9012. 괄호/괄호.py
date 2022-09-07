import sys

t = int(sys.stdin.readline())
for i in range(0, t):
    st = 0
    string = sys.stdin.readline()
    for c in string:
        if c == '(':
            st += 1
        elif c == ')':
            if st == 0:
                print('NO')
                break
            else:
                st -= 1
        else:
            if st == 0:
                print('YES')
            else:
                print('NO')