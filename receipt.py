receipt=int(input())
number=int(input())
sum=0
for i in range(number):

    a,b=map(int,input().split())

    sum+=(a*b)

if receipt == sum:
    print('Yes')

else:
    print('No')


