class A:
    def f1(self):
        print("f1 in A")
    def f2(self):
        print("f2 in A")


class B(A):
    def f1(self):
        print("f1 in B")

    def f1a(self):
        A().f1()


class C(B):
    def f1(self):
        print("f1 in C")

    def f1b(self):
        B().f1()


a = C()
a.f1()
a.f1a()
a.f1b()
a.f2()
