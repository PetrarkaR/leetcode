code = [5,7,1,4]
length = len(code)
code =code * 3
trueLen=len(code)
print(code)
empty=[]
i=0
k=3
if k > 0:
    for i in range(length, length+length):
        tmp=0
        j=0
        while(j<k):
            tmp+=code[i+j+1]
            j=j+1
            code[i]=tmp

if(k<0):
    for i in range(length+length-1, length-1,-1):
        tmp=0
        j=0
        while(j<abs(k)):
            tmp+=code[i-j-1]
            j=j+1
            code[i]=tmp
if(k==0):
    for i in range(length,trueLen):
        code[i]=0
        
modified_portion = code[length:2 * length]
print("Modified middle portion:", modified_portion)
