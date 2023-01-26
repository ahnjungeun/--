# https://www.acmicpc.net/problem/10773

l=[]
for _ in range(int(input())):
  i = int(input())
  if i==0:
    l.pop()
  else:
    l.append(i)
print(sum(l))