rows = int(input())
columns = rows
total = 0

matrix = []

for _ in range(rows):
    row = list(input())
    matrix.append(row)

sign = input()
found = False

for i in range(rows):
    if found:
        break
    for j in range(columns):
        if matrix[i][j] == sign:
            found = True
            print(f"({i}, {j})")
            break

if not found:
    print(f"{sign} does not occur in the matrix")