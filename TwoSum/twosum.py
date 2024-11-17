list = [1,5,7,8,3,4,6]
target=7
finger=0
retList=[1,2]

i=0
j=0
length=len(list)
for i in range (length):
    finder=target-list[i]
    for j in range(i+1,length):
        if(list[i]+list[j]==target):
            print(i,j)
