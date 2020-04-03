#Matrix Addition Program in Python

m1 = [[1,2,3],[4,2,6],[8,9,3]]
m2 = [[1,3,9],[4,8,2],[7,1,9]]
result =[[0,0,0,],[0,0,0],[0,0,0]]

#for rows 
for i in range(len(m1)):
    #for columns
    for j in range(len(m2)):
        result[i][j]=m1[i][j]+m2[i][j]

#resulted matrix
for i in result:
    print(i)
