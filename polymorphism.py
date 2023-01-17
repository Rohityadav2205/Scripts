"""
polymorphism
"""

def add(a=0,b=0,c=0):
    print(a,b,c)
    return a+b+c

a=add(1)
print(a)
a=add(1,2)
print(a)
a=add(1,2,3)
print(a)
