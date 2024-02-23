rows = cols = int(input())
current_row = 0
current_col = 0

dead = False

matrix = []

enemies = 0

armour = 300

for row in range(rows):
    str_row = input()
    matrix.append([])

    for col, char in enumerate(str_row):
        if char == "J":
            current_row = row
            current_col = col
        elif char == "E":
            enemies += 1

        matrix[row].append(char)

while True:
    command = input()

    matrix[current_row][current_col] = "-"

    if command == "left":
        current_col -= 1

        if current_col < 0:
            current_col = cols - 1

        sign = matrix[current_row][current_col]
    
    elif command == "right":
        current_col += 1

        if current_col > cols - 1:
            current_col = 0

        sign = matrix[current_row][current_col]

    elif command == "down":
        current_row += 1

        if current_row > rows - 1:
            current_row = 0

        sign = matrix[current_row][current_col]

    elif command == "up":
        current_row -= 1

        if current_row < 0:
            current_row = rows - 1

        sign = matrix[current_row][current_col]

    if sign == "E":
        armour -= 100
        enemies -= 1

    elif sign == "R":
        armour = 300
    
    matrix[current_row][current_col] = "J"

    if armour == 0:
        print(f"Mission failed, your jetfighter was shot down! Last coordinates [{current_row}, {current_col}]!")
        break
    elif enemies == 0:
        print("Mission accomplished, you neutralized the aerial threat!")
        break

for row in matrix:
    print("".join(row))
