list1=[]
while True:

    try:
        a,b=map(int,input().split())
        list1.append(a+b)
        

    except:
        break
    
for i in list1:
    print(i)


