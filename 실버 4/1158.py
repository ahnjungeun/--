# https://www.acmicpc.net/problem/1158

from collections import deque
a,b = map(int,input().split())
l=deque(range(1,a+1))
r=[]
while l:
  for i in range(b-1):
    l.append(l.popleft())
  r.append(l.popleft())
print(str(r).replace('[','<').replace(']','>'))