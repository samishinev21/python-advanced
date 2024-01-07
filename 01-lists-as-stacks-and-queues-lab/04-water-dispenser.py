from collections import deque

quantity_water = int(input())
queue = deque()

while True:
    command = input()

    if command == "Start":
        break
    else:
        queue.append(command)

while True:

    command = input()

    tokens = command.split(" ")

    if command == "End" or len(queue) == 0:
        print(f"{quantity_water} liters left")
        break
    elif command.isdecimal():
        quantity = int(command)

        if quantity > quantity_water:
            person = queue[0]

            print(f"{person} must wait")

        else:
            quantity_water -= quantity
            
            person = queue.popleft()

            print(f"{person} got water")
    elif tokens[0] == "refill":
        quantity_water += int(tokens[1])