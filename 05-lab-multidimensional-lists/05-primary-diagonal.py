rows = int(input())
total = 0

matrix = []

for _ in range(rows):
    row = list(map(int, input().split(" ")))
    matrix.append(row)

for i in range(rows):
    total += matrix[i][i]

print(total)