import sys
n = int(sys.stdin.readline())
list1=[]
list2=[]
case=0
number=0

for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    list1.append(a+b)
    
    list2.append(a)
    list2.append(b)

for i in list1:
    case+=1

    print('Case #{0}: {1} + {2} = {3}'.format(case,list2[number],list2[number+1],i))
    
    number+=2
