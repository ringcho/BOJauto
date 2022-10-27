import sys
string = sys.stdin.readline().strip()

patterns = {'c=':0,
            'c-':0,
            'dz=':0,
            'd-':0,
            'lj':0,
            'nj':0,
            's=':0,
            'z=':0}
temp = 0
for pattern in patterns:
    patterns[pattern] = string.count(pattern)
    if pattern == 'z=':
        patterns[pattern] = patterns[pattern] - patterns['dz=']
for pattern in patterns:
    if patterns[pattern]>0:
        temp += patterns[pattern] * (len(pattern)-1)

res = len(string)-temp

print(res,)