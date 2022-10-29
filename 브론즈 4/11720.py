# https://www.acmicpc.net/problem/11720

a,b = map(int,open(0))
sum = 0
for i in str(b):
  sum += int(i)
print(sum)