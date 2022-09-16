import sys
testCase = int(sys.stdin.readline())

numList=[]
scoreList=[]
averageList=[]
averageNum=0
overAverage=[]
for i in range(testCase):
    scoreAndnum = map(int,sys.stdin.readline().split())
    scoreAndnum=list(scoreAndnum)
    scoreList.append(scoreAndnum)
    numList.append(scoreList[i][0])
    del scoreList[i][0] #순서리스트 성적리스트 분리

for i in scoreList:
    averageList.append(sum(i)/len(i))

for i in scoreList:
    averagePoint=0
    for j in i:
        if j > averageList[averageNum]:
            averagePoint+=1

    overAverage.append((averagePoint/len(i))*100)


    averageNum+=1

for i in overAverage:
    print("{:.3f}%".format(i))








