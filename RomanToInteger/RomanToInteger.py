testString= "XLII"
length= len(testString)
array=list(testString)


roman_values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,

}
number_array = [roman_values[char] for char in array]


print(number_array)

number=0
for i in range(length-1):
    if(number_array[i]<number_array[i+1]):
        number-=number_array[i];
    if(number_array[i]>number_array[i+1]):
        number+=number_array[i]
    if(number_array[i]==number_array[i+1]):
        number+=number_array[i]
number+=number_array[length-1]
print(number)