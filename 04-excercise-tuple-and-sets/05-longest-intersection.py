n = input()
result = {}

for _ in range(int(n)):
    tokens = input().split("-")
    start_0, end_0 = map(int, tokens[0].split(","))
    start_1, end_1 = map(int, tokens[1].split(","))

    set_0 = set(range(start_0, end_0 + 1))
    set_1 = set(range(start_1, end_1 + 1))

    if len(set_0 & set_1) > len(result):
        result = list(set_0 & set_1)

print(f"Longest intersection is {result} with length {len(result)}")