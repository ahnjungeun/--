# https://www.acmicpc.net/problem/11497

for _ in range(int(input())):
  input()
  l=sorted(map(int,input().split()))
  l=l[0::2]+l[1::2][::-1]
  s=0
  print(*l)
  for i in range(len(l)-1):
    s=max(s,abs(l[i+1]-l[i]))
  print(s)