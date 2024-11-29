number=3
power=2
result=1
temp=1
if(power==0):
    result=1

if(power>0):
    while(power>0):
        if(power%2!=0):
            result=result*number
            power=power-1
        power=power//2
        number=number*number
        
if(power<0):
    while(abs(power)>0):
        if(abs(power)%2!=0):
            temp=temp*number
            power=abs(power)-1
        power=abs(power)//2
        number=number*number
        result=1/temp
print(result)