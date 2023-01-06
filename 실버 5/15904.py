# https://www.acmicpc.net/problem/15904

s=input()
r='UCPC'
c=0
for i in r:
  if i in s:
    s=s[s.index(i)+1:]
    c+=1
if c==4:
  print('I love UCPC')
else:
  print('I hate UCPC')