import sys

num=int(sys.stdin.readline())

string1=input()
num_list=[]
for i in range(num):
    new_num=int(string1[i])
    num_list.append(new_num)

print(sum(num_list))
