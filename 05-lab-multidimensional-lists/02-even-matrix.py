rows =  int(input())

matrix = []
even_matrix = []

for _ in range(rows):
    row = list(map(int, input().split(", ")))
    matrix.append(row)

for i, row in enumerate(matrix):
    even_matrix.append([])
    for number in row:
        if number % 2 == 0:
            even_matrix[i].append(number)

print(even_matrix)