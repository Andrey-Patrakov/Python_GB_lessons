import os
path = "files/"
os.makedirs(path, exist_ok=True)

with open(path + "z_1_out.txt", "w", encoding="utf-8") as f:
    while True:
        line = input()
        if line.strip() == "":
            break
        f.write(line + "\n")
