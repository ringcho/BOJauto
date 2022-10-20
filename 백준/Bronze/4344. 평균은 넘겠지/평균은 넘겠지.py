import sys
N = int(sys.stdin.readline())
for _ in range(N):
    scores = list(map(int, sys.stdin.readline().split()))[1:]
    avg = sum(scores) / len(scores)
    cnt = 0
    for score in scores:
        if score > avg:
            cnt += 1
    print(f'{100*cnt/len(scores):.3f}%')