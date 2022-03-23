

def std_weight(height,gender):
    weight_man=(height**2*22)/10**4
    weight_girl=(height**2*21)/10**4
    
    if gender =='남자':
        print('키 {0}cm남자의 표준 체중은 {1:.2f}kg입니다.'.format(height,weight_man))
        
    elif gender =='여자':
        print('키 {0}cm여자의 표준 체중은 {1:.2f}kg입니다.'.format(height,weight_girl))


std_weight(175,'남자')
std_weight(166, '여자')