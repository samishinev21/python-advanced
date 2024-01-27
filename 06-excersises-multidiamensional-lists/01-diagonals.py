n = int(input())

primary = []
secondary = []
matrix = []

for _ in range(n):
    row = list(map(int, input().split(", ")))
    matrix.append(row)

for i in range(n):
    for j in range(n):
        if i == j:
            primary.append(matrix[i][j])
        
        if j == n - 1 - i:
            secondary.append(matrix[i][j])

print(f"Primary diagonal: {', '.join(map(str, primary))}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join(map(str, secondary))}. Sum: {sum(secondary)}")