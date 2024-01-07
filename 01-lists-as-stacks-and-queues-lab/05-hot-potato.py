from collections import deque

names = input().split(" ")
n = int(input())

queue = deque(names)

while len(queue) != 1:
    for i in range(n):
        if i + 1 == n:
            person = queue.popleft()
            print(f"Removed {person}")
        else:
            person = queue.popleft()
            queue.append(person)

winner = queue.popleft()

print(f"Last is {winner}")