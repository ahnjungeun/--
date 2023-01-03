# https://www.acmicpc.net/problem/1449

N,L = map(int,input().split())
l = sorted(map(int,input().split()))

c = 1
s = 0
for i in range(N-1):
  s+=l[i+1]-l[i]
  if s>L-1:
    c+=1
    s=0
print(c)