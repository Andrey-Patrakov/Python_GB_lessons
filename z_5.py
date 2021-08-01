from random import random, choice, randint
import os

path = "files/"
os.makedirs(path, exist_ok=True)

sum1 = 0
sum2 = 0
with open(path + "z_5.txt", "w", encoding="utf-8") as f:
    for i in range(randint(5, 100)):
        line = [round(random() * choice([10, 100, 1000, 10000]), 2) for j in range(randint(1, 50))]
        sum1 += sum(line)
        print(*line, file = f)

lines = []
with open(path + "z_5.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

for line in lines:
    sum2 += sum(
        [float(nums) for nums in line.strip().split()]
    )

print(sum1)
print(sum2)
