path = "files/"

lines = []
with open(path + "z_2_in.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"В файле {len(lines)} строк")
for num, line in enumerate(lines, start=1):
    print(f"В {num} строке {len(line.strip().split())} слов")
