array=[1,4,6,7,2]
for i in range(0,len(array)):
    for j in range(i,len(array)):
        if(array[i]==2*array[j]):
            output=True
output=False