from functools import reduce

print(
    reduce(lambda a, b : a + b, [i for i in range(100, 1000 + 1) if i % 2 == 0])
)

print(
    sum([i for i in range(100, 1000 + 1) if i % 2 == 0])
)