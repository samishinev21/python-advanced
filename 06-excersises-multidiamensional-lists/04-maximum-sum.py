def sum_matrix(x):
    total = 0

    for row in x:
        total += sum(row)

    return total

max_sum = 0
max_matrix = []

rows, cols = [int(n) for n in input().split()]
matrix = [list(map(int, input().split())) for _ in range(rows)]

for row in range(rows - 2):
    for col in range(cols - 2):
        current_matrix = [
            [matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]],
            [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]],
            [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]
        ]

        current_sum = sum_matrix(current_matrix)

        if current_sum >= max_sum:
            max_sum = current_sum
            max_matrix = current_matrix
            
print(f"Sum = {max_sum}")

for row in max_matrix:
    print(" ".join(map(str, row)))