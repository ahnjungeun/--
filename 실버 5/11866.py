# https://www.acmicpc.net/problem/11866

a,b = map(int,input().split())
l = [i for i in range(a,0,-1)]
res = []
while len(l) > 0:
  for i in range(b-1):
    l.insert(0,l.pop())
  res.append(l.pop())

print('<',end='')
print(*res,sep=', ',end='')
print('>')