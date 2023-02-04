# https://www.acmicpc.net/problem/1021

from collections import deque
n,m = map(int,input().split())
l = list(map(int,input().split()))
q = deque(range(1,n+1)) # 1234
# q.rotate(1) # 4123
# q.rotate(-1) # 2341
c=0
while l:
  if l[0] == q[0]:
    q.popleft()
    l.pop(0)
  else:
    if len(q)/2<=q.index(l[0]):
      q.rotate(1)
      c+=1
    else:
      q.rotate(-1)
      c+=1
print(c)