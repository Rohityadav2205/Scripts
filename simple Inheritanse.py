class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return "name={0},age={1},address={2}".format(self.name, self.age, self.address)


rr = Person("jayanta", "42", "lahore")
print(rr)


class Employee(Person):

    def __init__(self, name, age, address, salary, post):
        super().__init__(name, age, address)
        self.Person = Person
        self.salary = salary
        self.post = post

    def __str__(self):
        return "{0},Salary={1},Post={2}".format(Person.__str__(self), self.salary, self.post)


r = Employee("raone", 90, "banglore", 2000, "vp")
print(r)
