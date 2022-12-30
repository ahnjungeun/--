# https://www.acmicpc.net/problem/2217

n = int(input())
l = []
for _ in range(n):
  l.append(int(input()))
l.sort()
ans = 0
k = 0
for i in l:
  ans = max(i*(len(l)-k),ans)
  k+=1
print(ans)