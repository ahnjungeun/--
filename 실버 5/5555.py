# https://www.acmicpc.net/problem/5555

s=input()
c=0
for _ in range(int(input())):
  S=input()
  S=S+S
  if s in S:
    c+=1
print(c)