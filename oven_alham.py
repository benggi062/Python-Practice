now_hour,now_min = map(int, input().split())

add_min = int(input())

sli_hour, sli_min= divmod(add_min,60)

now_min +=sli_min
now_hour +=sli_hour

if now_min >=60:
    now_min-=60
    now_hour+=1

if now_hour>=24:
    now_hour-=24
    
print(now_hour,now_min)


