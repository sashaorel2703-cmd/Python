n = int(input())
matrix = []
correct= True
for i in range(n ** 2):
    matrix.append(list(map(int, input().split())))
for l in matrix:
    if len(l) != len(set(l)):
        correct = False
        break
for j in range(n ** 2):
    column = []
    for i in range(n ** 2):
        column.append(matrix[i][j])
        if len(column) != len(set(column)):
            correct = False
            break
for i in range(0, n ** 2, n):
    for j in range(0, n ** 2, n):
        square = set()
        for x in range(i, i + n):
            for y in range(j, j + n):
                square.add(matrix[x][y])
        if len(square) != n ** 2:
            correct = False
            break

if correct :
    print("correct")
else:
    print("incorrect")
