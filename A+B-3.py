import sys
n = int(sys.stdin.readline())
list1=[]
case=0
for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    list1.append(a+b)

for i in list1:
    case+=1
    print('Case #{0}: {1}'.format(case,i))
