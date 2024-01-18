n = int(input())
guests = set()

for _ in range(n):
    number = input()
    guests.add(number)

while True:
    command = input()

    if command == "END":
        break

    if command in guests:
        guests.remove(command)

print(len(guests))

for guest in sorted(guests):
    print(guest)