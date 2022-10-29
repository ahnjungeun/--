# https://www.acmicpc.net/problem/5554

a,b,c,d = map(int,open(0))
sec = (a+b+c+d)%60
min = (a+b+c+d)//60%60
print(min)
print(sec)