# https://www.acmicpc.net/problem/1789

n = int(input())
i=0
s=0
while s+i<=n:
  s+=i
  i+=1
print(i-1)