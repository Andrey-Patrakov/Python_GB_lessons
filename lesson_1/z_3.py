n = input("Введите число n: ")
nn = n+n
nnn = n+n+n
n_list = list(map(int, [n, nn, nnn]))
print(f'{n} + {nn} + {nnn} = ', sum(n_list))
