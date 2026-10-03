def print_matrix(matrix):
    for row in matrix:
        for n in row:
            print(f"{n:<3}", end="")
        print()


n, m, k = list(map(int, input().split()))
matrix = [[0 for j in range(m)] for i in range(n)]
for i in range(k):
    x, y = list(map(int, input().split()))
    matrix[x - 1][y - 1] = "*"

for i in range(n):
    for j in range(m):
        if matrix[i][j] == "*":
            if i != 0 and j != 0 and matrix[i - 1][j - 1] != "*":
                matrix[i - 1][j - 1] += 1
            if j != 0 and matrix[i ][j - 1] != "*":
                matrix[i][j - 1] += 1
            if i != 0 and matrix[i - 1][j ] != "*":
                matrix[i - 1][j] += 1
            if i !=  n - 1 and j != 0 and matrix[i + 1][j - 1] != "*":
                matrix[i + 1][j - 1] += 1
            if i != 0 and j != m - 1 and matrix[i - 1][j + 1] != "*":
                matrix[i - 1][j + 1] += 1
            if i  != n - 1 and j != m - 1 and matrix[i + 1][j + 1] != "*":
                matrix[i + 1][j + 1] += 1
            if i != n - 1 and matrix[i + 1][j ] != "*":
                matrix[i + 1][j] += 1
            if j != m - 1 and matrix[i ][j + 1] != "*":
                matrix[i][j + 1] += 1
print_matrix(matrix)
