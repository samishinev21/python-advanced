from collections import deque

matches = 0
every_worm = True

worms = list(map(int, input().split(" ")))
holes = deque(map(int, input().split(" ")))

while len(worms) > 0 and len(holes) > 0:
    current_worm = worms.pop()
    current_hole = holes.popleft()

    if current_worm == current_hole:
        matches += 1
    else:
        current_worm -= 3

        if current_worm > 0:
            worms.append(current_worm)
        else:
            every_worm = False

if matches > 0:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

if len(worms) == 0 and every_worm == True:
    print("Every worm found a suitable hole!")
elif len(worms) == 0:
    print("Worms left: none")
else:
    print(f"Worms left: {', '.join(map(str, worms))}")

if len(holes) == 0:
    print("Holes left: none")

else:
    print(f"Holes left: {', '.join(map(str, holes))}")