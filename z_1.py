my_list = [True, 1, .5, False, 256, [2, 15], (3, 16), {1: True}, set([1,2,3,4,5,6,7,8,9])]

for elem in my_list:
    if type(elem) is int:
        print('Целое')
    elif type(elem) is float:
        print('Вещественное')
    elif type(elem) is bool:
        print('Логический')
    else:
        for elem_type in tuple, list, dict, set:
            if type(elem) is elem_type:
                print(elem_type.__name__)
