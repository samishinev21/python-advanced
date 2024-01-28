rows, cols = [int(n) for n in input().split()]

A_ASCII = 97

matrix = []

for row in range(rows):
    matrix.append([])
    for col in range(cols):
        matrix[row].append(f"{chr(A_ASCII + row)}{chr(A_ASCII + col + row)}{chr(A_ASCII + row)}")

    

for row in matrix:
    print(" ".join(row))