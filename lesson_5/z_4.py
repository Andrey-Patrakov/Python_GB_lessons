def replace_num_name(s: str):
    nums = {
        "one": "один",
        "two": "два",
        "three": "три",
        "four": "четыре",
        "five": "пять",
        "six": "шесть",
        "seven": "семь",
        "eight": "восемь",
        "nine": "девять",
        "ten": "десять",
        "eleven": "одиннадцать",
        "twelve": "двенадцать"
    }

    out = ""
    for word in s.split():
        if word.lower() in nums:
            out += f"{nums[word.lower()].title() if word.istitle() else nums[word.lower()]} " # noqa
        else:
            out += f"{word} "

    return out.strip()


path = "files/"

p_in = path + "z_4_in.txt"
p_out = path + "z_4_out.txt"
with open(p_in, "r", encoding="utf-8") as f_in, open(p_out, "w", encoding="utf-8") as f_out: # noqa
    lines = f_in.readlines()
    print(
        *[replace_num_name(line.strip()) for line in lines],
        sep="\n",
        file=f_out
    )
