#Matrix Multplication Program in Python

m1 = [[1,2,3],[4,2,6],[8,9,3]]
m2 = [[1,3,9],[4,8,2],[7,1,9]]
result =[[0,0,0,],[0,0,0],[0,0,0]]

#for rows m1
for i in range(len(m1)):
    #for columns of m2
    for j in range(len(m2[0])):
        #for rows of m2
        for k in range(len(m2)):
            result[i][j]=result[i][j]+m1[i][k]+m2[k][j]

#resulted matrix
for i in result:
    print(i)
