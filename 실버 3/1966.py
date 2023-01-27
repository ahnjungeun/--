# https://www.acmicpc.net/problem/1966

from collections import deque
for _ in range(int(input())):
  n,m = map(int,input().split())
  l = deque(map(int,input().split()))
  ol = deque()
  c=0
  for i,d in enumerate(l):
    ol.append((i,d))

  p=-1
  while p!=m:
    if max(l)!=ol[0][1]:
      l.append(l.popleft())
      ol.append(ol.popleft())
    else:
      l.popleft()
      p=ol.popleft()[0]
      c+=1
  print(c)