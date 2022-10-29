# https://www.acmicpc.net/problem/2525

hour, b = map(int,input().split())
c = int(input())

minute = b+c
res_minute = 0

if(minute >= 60):
  add_hour = minute // 60
  add_minute = minute % 60
  res_minute += add_minute
  hour += add_hour
  if(hour>23):
    hour = hour % 24
  print(hour,res_minute)
else:
  print(hour,minute)