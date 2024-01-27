def number_to_str(x):
    if x < 0:
        return f"({x})"
    else:
        return str(x)

n = int(input())

primary = []
secondary = []
matrix = []
result_primary = ""
result_secondary = ""

for _ in range(n):
    row = list(map(int, input().split(" ")))
    matrix.append(row)

for i in range(n):
    for j in range(n):
        if i == j:
            primary.append(matrix[i][j])
        
        if j == n - 1 - i:
            secondary.append(matrix[i][j])

total_primary = sum(primary)
total_secondary = sum(secondary)

print(f"Primary diagonal: sum = {' + '.join(map(number_to_str, primary))} = {total_primary}")
print(f"Secondary diagonal: sum = {' + '.join(map(number_to_str, secondary))} = {total_secondary}")
print(f"Difference: |{total_primary} - {total_secondary}| = {abs(total_primary - total_secondary)}")