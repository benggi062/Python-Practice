number=int(input())
first_num=number
num=0
while True:
    ten_num=(number//10) #2 6

    one_num=number-(ten_num*10)#6 8
    
    new= ten_num+one_num #8 14
    if new > 9:
        new = new % 10

    number=one_num*10 + new #68 

    num+=1
    
    if first_num == number:
        break

    
print(num)
    