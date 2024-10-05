path = "files/"

lines = []
with open(path + "z_3_in.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

lines = [line for line in lines if '=' in line]
print(
    "Сотрудники с зарплатой меньше 20 000:",
    *[man.split("=")[0] for man in lines if int(man.split("=")[1]) < 20000],
    sep='\n\t• '
)

s = sum([float(line.split("=")[1]) for line in lines])
print(f"Средняя зарплата: {s / len(lines)}")
