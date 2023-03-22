# https://www.acmicpc.net/problem/11931

import sys
input=sys.stdin.readline
print(*sorted([int(input()) for _ in range(int(input()))])[::-1],sep='\n')