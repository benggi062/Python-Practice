import sys
list1=[]
set_num=set()
for i in range(10):
    num=int(sys.stdin.readline())
    list1.append(num)

for i in list1:
    num= i%42
    set_num.add(num)

print(len(set_num))
    
    