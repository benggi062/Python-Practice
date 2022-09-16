n=int(input())
print(n)
list1=[]
for i in range(n):
    a,b = map(int,input().split())
    list1.append(a+b)

for i in list1:
    print(i)
    