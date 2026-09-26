def print_matrix(matrix):
    for row in matrix:
        for n in row:
            print(f"{n:<3}", end="")
        print()


n = int(input())
m = int(input())

matrix = [[i * j for j in range(m)] for i in range(n)]

print_matrix(matrix)
