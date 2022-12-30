# https://www.acmicpc.net/problem/9012

n=int(input())
for k in range(n):
  l=[]
  r=0
  s = input()
  for p in s:
    if p =='(':
      l.append(p)
    else:
      try:
        l.pop()
      except:
        r=1
        break
  if len(l)==0 and r==0:
    print('YES')
  else:
    print('NO')