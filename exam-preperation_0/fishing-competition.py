rows = cols = int(input())
current_row = 0
current_col = 0

dead = False

tons = 0

matrix = []

for row in range(rows):
    str_row = input()
    matrix.append([])

    for col, char in enumerate(str_row):
        if char == "S":
            current_row = row
            current_col = col

        matrix[row].append(char)


print(matrix)
while True:
    command = input()

    if command == "collect the nets":
        break
    else:
        matrix[current_row][current_col] = "-"

    if command == "up":
        current_row -= 1

        if current_row < 0:
            current_row = rows - 1

        sign = matrix[current_row][current_col]

        if sign.isnumeric():
            tons += int(sign)
        elif sign == "W":
            print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. " +
                  "Last coordinates od the ship: [{current_row},{current_col}]")
            dead = True
            break

    elif command == "down":
        current_row += 1

        if current_row > rows - 1:
            current_row = 0

        sign = matrix[current_row][current_col]

        if sign.isnumeric():
            tons += int(sign)
        elif sign == "W":
            print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. " +
                  "Last coordinates od the ship: [{current_row},{current_col}]")
            dead = True
            break

    
    elif command == "right":
        current_col += 1

        if current_col > cols - 1:
            current_col = 0

        sign = matrix[current_row][current_col]

        if sign.isnumeric():
            tons += int(sign)
        elif sign == "W":
            print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. " +
                  "Last coordinates od the ship: [{current_row},{current_col}]")
            dead = True
            break
    
    elif command == "left":
        current_col -= 1

        if current_col < 0:
            current_col = cols - 1

        sign = matrix[current_row][current_col]
        
        if sign.isnumeric():
            tons += int(sign)
        elif sign == "W":
            print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. " +
                  "Last coordinates od the ship: [{current_row},{current_col}]")
            dead = True
            break
    
    matrix[current_row][current_col] = "S"


if not dead:
    if tons >= 20:
        print("Success! You managed to reach the quota!")
    else:
        print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - tons} tons of fish more.")

    print(f"Amount of fish caught: {tons} tons.")

    for row in matrix:
        print("".join(row))