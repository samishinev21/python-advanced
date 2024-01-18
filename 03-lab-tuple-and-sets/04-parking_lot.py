n = int(input())
cars_in_park = set()

for _ in range(n):
    command = input().split(", ")

    direction = command[0]
    number = command[1]

    if direction == "IN":
        cars_in_park.add(number)
    elif direction == "OUT":
        cars_in_park.remove(number)

if len(cars_in_park) <= 0:
    print("Parking Lot is Empty")
else:   
    for car in cars_in_park:
        print(car)