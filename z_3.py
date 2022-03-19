n = input("Введите число n: ")
nn = n+n
nnn = n+n+n
l = list(map(int, [n, nn, nnn]))
print(f'{n} + {nn} + {nnn} = ', sum(l))