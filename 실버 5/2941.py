# https://www.acmicpc.net/problem/2941

c=['c=','c-','dz=','d-','lj','nj','s=','z=']
s=input()
r=0
for i in c:
  r+=s.count(i)
  s=s.replace(i,'1')
print(len(s))