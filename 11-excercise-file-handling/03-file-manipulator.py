import os

while True:
    command = input()

    if command == "End":
        break

    tokens = command.split("-")
    
    if tokens[0] == "Create":
        try:
            file = open(tokens[1], "x")
        except FileNotFoundError:
            file = open(tokens[1], "w")
            file.write("")
        finally:
            file.close()          

    elif tokens[0] == "Add":
        try:
            file = open(tokens[1], "a")
            file.write(f"{tokens[2]}\n")
        except FileNotFoundError:
            file = open(tokens[1], "x")
            file.write(f"{tokens[2]}\n")
        finally:
            file.close()

    elif tokens[0] == "Replace":
        try:
            input_file = open(tokens[1], "r")
            
            lines = []
            for line in input_file:
                lines.append(line.replace(tokens[2], tokens[3]))

            output_file = open(tokens[1], "w")
            output_file.writelines(lines)

            output_file.close()
        except FileNotFoundError:
            print("An error occurred")

    elif tokens[0] == "Delete":
        try:
            os.remove(tokens[1])
        except FileNotFoundError:
            print("An error occurred")