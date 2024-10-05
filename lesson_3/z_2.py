def print_in_one_line(name, surname, birth, city, email, tel_number):
    my_string = f'{surname} {name} {birth} года рождения, '
    my_string += f'проживает в г. {city}, email: {email}, номер телефона: {tel_number}' # noqa
    print(my_string)


name = input("Введите имя: ")
surname = input("Введите фамилию: ")
birth = input("Введите год рождения: ")
city = input("Введите город проживания: ")
email = input("Введите email: ")
tel_number = input("Введите номер телефона: ")

print_in_one_line(name=name,
                  surname=surname,
                  birth=birth,
                  city=city,
                  email=email,
                  tel_number=tel_number)
