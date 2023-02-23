# https://www.acmicpc.net/problem/14425

n,m=map(int,input().split())
S = [input() for _ in range(n)]
M = [input() for _ in range(m)]
c=0
for i in M:
  if i in S:
    c+=1
print(c)