triangle= [[1]]
future = []
past = [0]
test = []
print(triangle)
placeholder=0
n=5
elements=1
for i in range(1,n,1):
    
    elements=elements+1
    
    future=past*(elements)
    triangle.append(future)
    triangle[i][0]=1
    triangle[i][elements-1]=1
    for j in range(1,elements-1,1):
        triangle[i][j]=triangle[i-1][j-1]+triangle[i-1][j]
        
print(triangle)
#     1
#   1   1
#  1  2  1
# 1  3 3  1
