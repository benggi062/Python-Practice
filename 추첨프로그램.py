from random import*
print('-- 당첨자 발표 --')
chicken=range(1,21)
chicken=list(chicken)
shuffle(chicken)
a=sample(chicken,1)
print('치킨 당첨자는:',' '.join(map(str,a)),'번 사용자 입니다.')
#구조변경
a=set(a)
chicken=set(chicken)
b=(chicken.difference(a))#차집합
#구조변경
b=list(b)
new_list=sample(b,3)
print('커피 당첨자는:',new_list,'번 사용자들 입니다.')
print('-- 축하합니다 --')


















