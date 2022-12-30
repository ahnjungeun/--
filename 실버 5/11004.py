# https://www.acmicpc.net/problem/11004

a,b = map(int,input().split())
num_list = map(int,input().split())
num_list = list(num_list)
num_list.sort()
print(num_list[b-1])