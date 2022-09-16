import sys

n=int(sys.stdin.readline())

score=map(int,sys.stdin.readline().split())

score=list(score)

max_num=max(score)

sum_list=0
for i in score:
    oper_num=(i/max_num)*100
    sum_list+=oper_num
    

print(sum_list/n)


