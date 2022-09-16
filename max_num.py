import sys
num_list=[]
for i in range(9):
    num=int(sys.stdin.readline())
    num_list.append(num)


max_num=max(num_list)

num_index=num_list.index(max_num)

print(max_num)

print(num_index+1)