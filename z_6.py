import os

def find_time(s):
    my_list = ["(л)", "(пр)", "(лаб)"]
    for l in my_list:
        if s.find(l) != 0:
            num = s.split(l)[0]
            if num.isdigit():
                return int(num)

    return 0

path = "files/"
os.makedirs(path, exist_ok=True)

lines = []
with open(path + "z_6_in.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

my_dict = {}
for line in lines:
    if ":" in line:
        lesson, line = line.split(":")
        lesson = lesson.split()[-1]
        s = sum(find_time(word) for word in line.split())
        my_dict[lesson] = s

print(my_dict)
            
