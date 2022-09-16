dnList=[]
selfNumlist=[]

def d(n):
    if n<10 and n>0: #1의자리
        n+=n

    elif n >=10 and n <100: #10의 자리
        n=str(n)
        n10=int(n[0])
        n1=int(n[1])
        n=int(n)
        n+=(n10+n1)

    elif n >=100 and n < 1000: #100의 자리
        n=str(n)
        n100=int(n[0])
        n10=int(n[1])
        n1=int(n[2])
        n=int(n)
        n+=(n100+n10+n1)
        
    elif n >=1000 and n <=10000: #1000의 자리
        n=str(n)
        n1000=int(n[0])
        n100=int(n[1])
        n10=int(n[2])
        n1=int(n[3])
        n=int(n)
        n+=(n1000+n100+n10+n1)

    return n


    



    