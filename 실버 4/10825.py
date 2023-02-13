# https://www.acmicpc.net/problem/10825

N=int(input())
l=[]
for _ in range(N):
  n,k,e,m = input().split()
  l.append((n,int(k),int(e),int(m)))
l.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))
for i in l:
  print(i[0])