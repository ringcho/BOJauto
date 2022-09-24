
N, K = map(int, input().split())

queue = [i for i in range(1, N+1)]
Josephus = []

while queue:
    for _ in range(K-1):
        tmp = queue.pop(0)   
        queue.append(tmp) 
    dead = queue.pop(0)    
    Josephus.append(dead)

print('<'+', '.join(map(str, Josephus))+'>')