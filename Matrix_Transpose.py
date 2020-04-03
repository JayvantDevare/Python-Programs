#Matrix Transpose Program in Python

m1 = [[1,2,3],[4,2,6],[8,9,7]]

result =[[0,0,0,],[0,0,0],[0,0,0]]

#for rows 
for i in range(len(m1)):
    #for columns
    for j in range(len(m1[0])):
        result[j][i]=m1[i][j]

#Original matrix
for i in m1:
    print(i)
    
print("\n Transpose of given matrix\n")

#resulted matrix
for i in result:
    print(i)
