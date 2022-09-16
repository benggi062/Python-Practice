import sys

list1=[]
while True:
    a,b=map(int,sys.stdin.readline().split())
    if a == 0 and b==0:
        break

    list1.append(a+b)
    

for i in list1:
    print(i)
