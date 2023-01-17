class A:
    def __init__(self,name=None):  #constructor
        print("In constructor is called ")
        self.name=name
    def __str__(self):
        return  'name={0}'.format(self.name)
    def __del__(self):
        print("Destructor is called ")
v=A('Rohit')  #object
print(v)