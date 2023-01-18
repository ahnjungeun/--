# https://www.acmicpc.net/problem/1065

n=int(input())
if n<100:
  print(n)
else:
  c=99
  for i in range(100,n+1):
    if i==1000:
      break
    i=str(i)
    if int(i[0])-int(i[1])==int(i[1])-int(i[2]):
      c+=1
  print(c)