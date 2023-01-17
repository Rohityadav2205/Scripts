""" Encapsulation

"""


class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return '{0},{1},{2}'.format(self.name, self.age, self.address)


class Ticket:
    def __init__(self, train_name, number, passenger):
        self.train_name = train_name
        self.number = number
        self.passenger = passenger

    def __str__(self):
        return '{0},{1},{2}'.format(self.train_name, self.number, self.passenger)


t = Ticket('lokmanyatilak', '12360', Person('Rohit', 24, 'varanasi'))
print(t)
