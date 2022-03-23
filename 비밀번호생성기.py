site='http://daum.net'

first_password=site[7:10]
site=site.replace('http://',"")
site=site[:site.index('.')]
second_password=len(site)

third_password=site.count('e')

password=str(first_password)+str(second_password)+str(third_password)+'!'
print('{0}의 비밀번호는 {1}입니다.'.format('http://daum.net',password))













