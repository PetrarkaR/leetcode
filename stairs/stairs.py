from math import factorial

number = 9 
result=0

max_twos = number // 2


for twos in range(max_twos + 1):
    ones = number - 2 * twos  # Remaining positions are "1-blocks"
    if ones < 0:
        break  
    
    result += factorial(twos + ones) // (factorial(twos) * factorial(ones))
    print(result)
