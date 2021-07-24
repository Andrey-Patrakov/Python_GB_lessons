def int_func(s):
    return s.capitalize()

s = list(map(int_func, input("Введите слова разделённые пробелом\n").split()))
s = ' '.join(s)
print(s)

print('абв гдеёжз ийкл мнопр'.title())