import sys

n,x=map(int,sys.stdin.readline().split())

num_list=map(int,sys.stdin.readline().split())

num_list=list(num_list)
last_list=[]
for i in num_list:
    if i < x:
        last_list.append(i)

print(*last_list)






    
    







