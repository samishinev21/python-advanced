n, m = map(int, input().split(" "))

n_set = set()
m_set = set()

for _ in range(n):
    num = input()

    n_set.add(num)

for _ in range(m):
    num = input()

    m_set.add(num)

intersection = n_set & m_set

for num in intersection:
    print(num)