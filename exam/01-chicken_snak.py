from collections import deque

money = list(map(int, input().split(" ")))
price = deque(map(int, input().split(" ")))
eaten_food = 0


while len(money) > 0 and len(price) > 0:
    current_money = money.pop()
    current_price = price.popleft()

    if current_money == current_price:
        eaten_food += 1

    elif current_money > current_price:
        eaten_food += 1
        if len(money) > 0:
            change = current_money - current_price
            money[len(money) - 1] += change

if eaten_food >= 4:
    print(f"Gluttony of the day! Henry ate {eaten_food} foods.")

elif eaten_food > 1:
    print(f"Henry ate: {eaten_food} foods.")

elif eaten_food == 1:
    print(f"Henry ate: {eaten_food} food.")

else:
    print("Henry remained hungry. He will try next weekend again.")