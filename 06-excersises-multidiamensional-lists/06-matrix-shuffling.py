rows, cols = [int(n) for n in input().split()]

matrix = [input().split() for _ in range(rows)]

while True:
    tokens = input().split(" ")
    command = tokens[0]

    if command == "END":
        break
    elif command == "swap":
        source_row = int(tokens[1])
        source_col = int(tokens[2])

        target_row = int(tokens[3])
        target_col = int(tokens[4])

        if (0 <= source_row < rows and 0 <= source_col < cols and
            0  <= target_row < rows and 0 <= target_col < cols):
            matrix[source_row][source_col], matrix[target_row][target_col] = \
                matrix[target_row][target_col], matrix[source_row][source_col]
            
            for row in matrix:
                print(" ".join(map(str, row)))

        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
