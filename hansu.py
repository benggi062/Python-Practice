import sys

n=int(sys.stdin.readline())

def hansu(n,numPoint=0):
    
    for i in range(1,n+1):
            
        if i < 100:
            numPoint+=1
            continue
            
        i=str(i)
        n100 = int(i[0])
        n10= int(i[1])
        n1 = int(i[2])
        i=int(i)
        up0 = (n10-n100) * (n1-n10) >=0
        if up0 and (n10-n100 == n1-n10):
            numPoint+=1

    return numPoint

print(hansu(n))

                



        
        

