mat1 = [
    [2, 4],
    [3, 1],
]

mat2 = [
    [7, 2],
    [5, 6],
]
mat3 = []

def perkalianMatrix():
    for x in range(0, len(mat1)):
        row = []
        for y in range(0,len(mat1[0])):
            total = 0
            for z in range(0, len(mat1[0])):
                total = total + (mat1[x][z] * mat2 [z][y])
            row.append(total)
        mat3.append(row)

    for x in range(0, len(mat3)):
        for y in range(0, len(mat3[0])):
            print(mat3[x][y], end=' ')
        print()

perkalianMatrix()

#perkalian matrix

