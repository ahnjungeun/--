# https://www.acmicpc.net/problem/2606

n=int(input())
e=int(input())
M = [[] for _ in range(n+1)]

for _ in range(e):
  a,b = map(int,input().split())
  M[a].append(b)
  M[b].append(a)
  
for i in M:
  i.sort()
  
visited = [0] * (n+1)

def dfs(v):
  visited[v] = 1
  for i in M[v]:
    if not visited[i]:
      dfs(i)

dfs(1)
print(visited.count(1)-1)