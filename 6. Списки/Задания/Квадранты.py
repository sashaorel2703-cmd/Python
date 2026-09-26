def print_matrix(matrix):
    for row in matrix:
        for n in row:
            print(f"{n:<3}", end="")
        print()


n = int(input())
matrix = [[0 if (i + j) == n - 1 or i == j \
               else 1 if i < j and j + i < n \
    else 2 if i < j and j + i >= n \
    else 3 if i > j and j + i >= n \
    else 4
           for j in range(n)]
          for i in range(n)]

print_matrix(matrix)
