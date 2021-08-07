class Worker:

    _income = dict()

    def __init__(self, name, surname, position, income: dict):
        self.name = name
        self.surname = surname
        self.position = position
        
        if type(income) is not dict:
            raise ValueError('Неверно передан параметр "income"')
            
        if 'wage' in income and 'bonus' in income:
            self._income['wage'] = income['wage']
            self._income['bonus'] = income['bonus']
            return
        
        raise ValueError('Неверно заполнен параметр income') 
            
class Position(Worker):
    
    def __init__(self, name, surname, position, income: dict):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return f'{self.surname} {self.name}'
    
    def get_total_income(self):
        return sum([a for a in self._income.values()])

try:
    Ivan = Position('Иван', 'Иванов', 'Водитель', {'wage':30000, 'bonus':5000})

    print(Ivan.name)
    print(Ivan.surname)
    print(Ivan.position)

    print(Ivan.get_full_name())
    print(Ivan.get_total_income())

except Exception as e:
    print(e)