#구구단
x = int(input("보고싶은 단을 입력하세요.: "))# 몇단을 볼건지 입력받음

y=1

while y<10:#루프
    
    print(str(x),'*',str(y),'=',str(x*y).rjust(3))
    y+=1
    