x=int(input('숫자를 입력하세요: '))
i=1
while i<=x:
    sum = '*'*i
    print(str(sum).rjust(x))
    i+=1
