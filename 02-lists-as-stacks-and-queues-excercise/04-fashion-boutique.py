clothes_in_box = map(int, input().split(" "))
capacity_rack = int(input())
number_racks = 1
rack = []

for cloth in clothes_in_box:
    if sum(rack) + cloth > capacity_rack:
        rack = []
        number_racks += 1

    rack.append(cloth)

print(number_racks)