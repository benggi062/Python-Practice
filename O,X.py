import sys

test_case_num=int(sys.stdin.readline())
oxlist=[]
score_list=[]

for i in range(test_case_num):
    o_x=sys.stdin.readline()
    oxlist.append(o_x)

for i in oxlist:
    score=0
    last_score=0
    for j in i:
        score+=1

        if j =='O':
            last_score+=score

        else:
            score = 0
    score_list.append(last_score)

for i in score_list:
    print(i)
    
    


    
    
