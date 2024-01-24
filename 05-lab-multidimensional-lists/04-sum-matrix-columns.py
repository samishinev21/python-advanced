rows, columns = map(int, input().split(", "))
total = 0

matrix = []

for _ in range(rows):
    row = list(map(int, input().split(" ")))
    matrix.append(row)

for i in range(columns):
    total = 0
    for j in range(rows):
        total += matrix[j][i]
    print(total)