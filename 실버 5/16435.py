# https://www.acmicpc.net/problem/16435

n,m=map(int,input().split())
l=sorted(map(int,input().split()))
for i in l:
  if m>=i:
    m+=1
print(m)