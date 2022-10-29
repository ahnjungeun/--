# https://www.acmicpc.net/problem/2747

n = int(input())
res = [0,1,1]
if n == 0:
  print(0)
elif n == 1 or n == 2:
  print(1)
else:
  for i in range(n-2):
    res.append(res[i+1]+res[i+2])
  print(res[n])