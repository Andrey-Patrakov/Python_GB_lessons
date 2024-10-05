earn = int(input('Введите выручку: '))
expense = int(input('Введите расходы: '))

if earn > expense:
    profit = earn - expense
    print(f'Прибыль предприятия составляет {profit} руб')
    print(f'Рентабельность выручки составляет {profit / earn}')
    man_count = int(input('Введите численность сотрудников фирмы: '))
    print(f'Прибыль фирмы в расчете на одного сотрудника: {profit / man_count} руб')  # noqa

elif expense > earn:
    print(f'Убыток предприятия составляет {expense - earn} руб')
else:
    print('У предприятия дохода нет')
