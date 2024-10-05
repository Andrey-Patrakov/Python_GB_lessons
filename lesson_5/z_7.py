from numpy import mean
import json

path = "files/"
lines = []
with open(path + "z_7.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

my_dict = {}
for line in lines:
    line = line.split()
    my_dict[line[0]] = float(line[2]) - float(line[3])

my_list = [
    my_dict,
    {"average_profit":
        round(mean([profit for profit in my_dict.values() if profit >= 0]), 2)}
]

with open(path + "z_7_out.json", "w") as f:
    json.dump(my_list, f)
