# https://www.acmicpc.net/problem/1085

x,y,w,h = map(int,input().split())
res = [x-0,y-0,w-x,h-y]
print(min(res)) # print(min([x,y,w-z,h-y])) ㄱㄴ