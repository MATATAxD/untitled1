class A:
    def f0(self):
        print('A.f0')
    def f1(self):
        print('A.f1')
        self.f0()
class B(A):
    def f0(self):
        print('B.f0')
        self.f4()
    def f4(self):
        print('B.f4')
class C(B):
    def f0(self):
        print('C.f0')
    def f3(self):
        print('C.f3')
    def f4(self):
        print('C.f4')



c=B()
c.f3()