# https://www.acmicpc.net/problem/9237

n=c=int(input())
l=sorted(map(int,input().split()))[::-1]
r=[]
for i in l:
  r.append(i-c+2)
  c-=1
print(max(r)+n)