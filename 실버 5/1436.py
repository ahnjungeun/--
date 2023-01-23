# https://www.acmicpc.net/problem/1436

n = int(input())
c = 0
i = 666
while c != n:
  if '666' in str(i):
    c+=1
  i+=1
print(i-1)