class MyDate:

    def __init__(self, s):
        try:
            day, month, year = [int(i) for i in s.split("-")]

        except Exception:
            month, year = [int(i) for i in s.split("-")]
            self.__with_day = False
            MyDate.is_valid(month=month, year=year, raise_flag=True)
            self.__month = month
            self.__year = year

        else:
            MyDate.is_valid(day=day, month=month, year=year, raise_flag=True)
            self.__with_day = True
            self.__day = day
            self.__month = month
            self.__year = year

    def __str__(self):
        s = ""
        if self.__with_day:
            s += str(self.__day).zfill(2) + "-"

        s += str(self.__month).zfill(2) + "-"
        s += str(self.__year).zfill(4)
        return s

    @classmethod
    def from_values(cls, day, month, year=None):
        if year:
            return MyDate(f'{day}-{month}-{year}')

        return MyDate(f'{day}-{month}')

    @staticmethod
    def is_valid(**kwargs):
        is_day = False
        raise_flag = False

        if "raise_flag" in kwargs.keys():
            raise_flag = True

        try:
            if "day" in kwargs.keys():
                is_day = True
                if kwargs["day"] < 1:
                    raise ValueError("Некорректно указан день")

            if kwargs["month"] in (1, 3, 5, 7, 8, 10, 12):
                if is_day and kwargs["day"] > 31:
                    raise ValueError("Некорректно указан день")

            elif kwargs["month"] in (4, 6, 9, 11):
                if is_day and kwargs["day"] > 31:
                    raise ValueError("Некорректно указан день")

            elif kwargs["month"] == 2:
                if is_day:
                    if kwargs["year"] % 4 == 0:
                        if kwargs["day"] > 29:
                            raise ValueError("Некорректно указан день")
                    elif kwargs["day"] > 28:
                        raise ValueError("Некорректно указан день")

            else:
                raise ValueError("Некорректно указан месяц")

        except Exception as e:
            if raise_flag:
                raise e

            return False

        return True


print(MyDate("21-11-2015"))
print(MyDate("1-01-2015"))
print(MyDate("11-2015"))
print(MyDate.from_values(21, 11, 2015))
print(MyDate.from_values(11, 2015))

print()
print(MyDate.is_valid(day=13, month=2, year=2021))
print(MyDate.is_valid(day=-1, month=2, year=2021))  # некорректная дата
try:
    # некорректная дата
    print(MyDate.is_valid(day=-1, month=2, year=2021, raise_flag=True))
except Exception as e:
    print(e)

print()
print(MyDate("29-02-2020"))  # високосный год
try:
    print(MyDate("29-02-2021"))  # невисокосный год
except Exception as e:
    print(e)
