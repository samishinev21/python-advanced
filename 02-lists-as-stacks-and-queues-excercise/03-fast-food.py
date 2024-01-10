from collections import deque

food_quantity = int(input())
orders = input().split(" ")
biggest = 0

queue_orders = deque()

for n in orders:
    queue_orders.append(int(n))

for order in queue_orders:
    if order > biggest:
        biggest = order

print(biggest)

while len(queue_orders) > 0:
    if food_quantity >= queue_orders[0]:
        food_quantity -= queue_orders.popleft()
    else:
        break

if len(queue_orders) == 0:
    print("Orders complete")
else:
    print(f"Orders left: ", end="")
    while len(queue_orders) > 0:
        if len(queue_orders) == 1:
            print(queue_orders.popleft(), end="")
        else:
            print(queue_orders.popleft(), end=" ")