from collections import deque

rows, cols = [int(n) for n in input().split()]

word = deque(input() * rows * cols)
matrix = []

for row in range(rows):
    matrix.append([])
    for _ in range(0, cols):
        matrix[row].append(word.popleft())
    if row % 2 != 0:
        matrix[row] = list(reversed(matrix[row]))
        
for list in matrix:
    print("".join(list))    