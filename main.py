import datetime


class Employee:
    num_of_emps = 0
    raise_coef = 1.5

    def __init__(self, name, surname, pay):
        self.name = name
        self.surname = surname
        self.__email = name.lower() + '.' + surname.lower() + '@email.com'
        self.__pay = pay

        Employee.num_of_emps += 1



    def raise_pay(self):
        self.__pay = int(self.__pay * self.raise_coef)

    @classmethod
    def from_string(cls, data_string):
        name, surname, pay = data_string.split(' ')
        pay = int(pay)
        return cls(name, surname, pay)

    @classmethod
    def set_raise_amt(cls, new_coef):
        cls.raise_coef = new_coef

    @staticmethod
    def is_workday():
        now = datetime.datetime.now()
        if now.weekday() == 5 or now.weekday() == 6:
            return False
        return True

    @property
    def email(self):
        return self.__email

    @property
    def pay(self):
        return self.__pay


if __name__ == '__main__':

    emp_1 = Employee('Ivan', 'Ivanov', 60000)

    # TestCase#1 Email
    assert emp_1.email == 'ivan.ivanov@email.com'

    # TestCase#2 RaisePay
    emp_1.raise_pay()
    assert 60000 * Employee.raise_coef == emp_1.pay
    assert emp_1.pay == 90000

    # TestCase#3 New objet
    emp_2 = Employee.from_string('Petr Petrov 70000')
    assert isinstance(emp_2, Employee)
    assert emp_2.name == 'Petr'
    assert emp_2.surname == 'Petrov'
    assert emp_2.pay == 70000

    # TestCase#4 Set raise amount
    Employee.set_raise_amt(2)
    assert Employee.raise_coef == 2
    assert emp_1.raise_coef == 2
    assert emp_2.raise_coef == 2

    #TestCase#5 Is working
    assert Employee.is_workday() == True
