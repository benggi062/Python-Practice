from random import*
person=1
count=0
while person <= 50:
    
    maching_time =randint(5,50)
    print('[O] {0} 번째 손님 (소요시간: {1}분)'.format(person,maching_time))
    person +=1
    
    if 5<=maching_time and maching_time <=15:
        count +=1

print('총 탑승 승객은 {0} 명 입니다.'.format(count))


    

    