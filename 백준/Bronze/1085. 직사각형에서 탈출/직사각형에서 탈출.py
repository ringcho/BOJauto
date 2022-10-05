x,y,w,h= map(int,input().split(" "))

distance = []

distance.append(abs(x-0))
distance.append(abs(y-0))
distance.append(abs(w-x))
distance.append(abs(h-y))
distance.sort()
print(distance[0])
