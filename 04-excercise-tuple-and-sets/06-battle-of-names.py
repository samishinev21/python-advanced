n = int(input())
names = {}
odd_set = set()
even_set = set()

for i in range(1, n + 1):
    current_sum = 0
    name = input()

    for letter in name:
        current_sum += ord(letter)

    current_sum = current_sum // i

    if (current_sum) % 2 == 0:
        even_set.add(current_sum)
    else:
        odd_set.add(current_sum)

sum_odd = sum(map(int, odd_set))
sum_even = sum(map(int, even_set))

if sum_odd == sum_even:
    union = odd_set | even_set
    print(", ".join(map(str, union)))
elif sum_odd > sum_even:
    difference = odd_set - even_set
    print(", ".join(map(str, difference)))
elif sum_even > sum_odd:
    symmetric_difference = odd_set ^ even_set
    print(", ".join(map(str, symmetric_difference)))
