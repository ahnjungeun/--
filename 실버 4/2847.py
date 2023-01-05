# https://www.acmicpc.net/problem/2847

n = int(input())
l = []
i=c=0
for _ in range(n):
  l.append(int(input()))
while i!=n-1:
  if l[i] >= l[i+1]:
    l[i]-=1
    c+=1
    i=0
  else:
    i+=1
print(c)