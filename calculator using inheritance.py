class A:
    num1=int(input("Enter First Number :"))
    num2=int(input("Enter Second Number :"))
    def Add(self):
        print("Addition",self.num1+self.num2)
    def Sub(self):
        print("Substraction",self.num1-self.num2)

class B(A):                 #Inherited all properties of class A
    def Multi(self):
        print("Multiplication",self.num1*self.num2)
    def Div(self):
        print("Division",self.num1/self.num2)
    def Rem(self):
        print("Reminder",self.num1%self.num2)
obj=B()
obj.num1
obj.num2
obj.Add()
obj.Sub()
obj.Multi()
obj.Div()
obj.Rem()