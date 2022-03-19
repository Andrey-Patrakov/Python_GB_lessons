t = int(input('Введите время в секундах: '))
hour = t // 3600
minute = t % 3600 
second = minute % 60
minute //= 60

print(f'{hour:02d}:{minute:02d}:{second:02d}')
