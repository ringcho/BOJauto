import sys
string = sys.stdin.readline()

match = {
    'ABC':2,
    'DEF':3,
    'GHI':4,
    'JKL':5,
    'MNO':6,
    'PQRS':7,
    'TUV':8,
    'WXYZ':9,
}
res = 0
for char in string:
    for key in match.keys():
        if char in key:
            res += match[key] + 1
print(res)