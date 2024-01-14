from collections import deque

amount_stations = int(input())
queue = deque()

for _ in range(amount_stations):
    litters, distance = map(int, input().split(" "))
    queue.append([litters, distance])

for start_station in range(amount_stations):
    queue_copy = queue.copy()
    total_litters = 0

    while len(queue_copy):
        litters, distance = queue_copy.popleft()
        total_litters += litters

        total_litters -= distance

        if total_litters < 0:
            queue.rotate(-1)
            break
    
    if len(queue_copy) == 0:
        print(start_station)
        break