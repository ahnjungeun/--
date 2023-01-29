# https://www.acmicpc.net/problem/2164

from collections import deque
l=deque(range(1,int(input())+1))
f=1
while len(l)!=1:
  if f:
    l.popleft()
    f=0
  else:
    l.append(l.popleft())
    f=1
print(*l)