# https://www.acmicpc.net/problem/1302

l=[]
r=set()
for _ in range(int(input())):
  l.append(input())
for i in l:
  r.add((l.count(i),i))
print(sorted(r,key=lambda x:(-x[0],x[1]))[0][1])