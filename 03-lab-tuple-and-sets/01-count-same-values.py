tuple = tuple(map(float, input().split(" ")))
unique_nums = {}

for num in tuple:
    if num not in unique_nums:
        unique_nums[num] = 0

    unique_nums[num] += 1

for num, count in unique_nums.items():
    print(f"{num} - {count} times")