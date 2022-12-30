# https://www.acmicpc.net/problem/1343

s = input()
s=s.replace('X','B')
s=s.replace('BBBB','AAAA')
s1 = s.replace('.',' ').split()
a=0
for i in s1:
  if len(i)%2==1:
    a=1
    break
print(s if a==0 else -1)