rows =  int(input())

matrix = []
my_matrix = []

for _ in range(rows):
    row = list(map(int, input().split(", ")))
    matrix.append(row)

for rows in matrix:
    for number in rows:
        my_matrix.append(number)

print(my_matrix)