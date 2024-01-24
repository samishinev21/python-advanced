rows, columns = map(int, input().split(", "))
total = 0

matrix = []

for _ in range(rows):
    row = list(map(int, input().split(", ")))
    matrix.append(row)

for row in matrix:
    for number in row:
        total += number

print(total)
print(matrix)