'''
在python 2.3及后续版本中，类均为新式类
class Foo(object),从object继承均为新式类
使用C3算法，解决钻石继承问题
'''
class A(object):
    def __init__(self):
        print('enter A')
        print('leave A')
    def prt(self):
        print('This is A method')

class B(object):
    def __init__(self):
        print('enter B')
        print('leave B')

class C(A):
    def __init__(self):
        print('enter C')
        super(C, self).__init__()
        print('leave C')

class D(A):
    def __init__(self):
        print('enter D')
        super(D, self).__init__()
        print('leave D')
    def prt(self):
        print('This is D method')

class E(B, C):
    def __init__(self):
        print('enter E')
        super(E, self).__init__()
        print('leave E')

class F(E, D):
    def __init__(self):
        print('enter F')
        super(F, self).__init__()
        print('leave F')

f = F()
print(F.__mro__)
f.prt()

'''
L[A] = [A,object]
L[B] = [B,object]
L[C] = [C,A,object]
L[D] = [D,A,object]
L[E] = [E] + merge(L[B],L[C],[B],[C])
     = [E] + merge([B,object],[C,A,object],[B],[C])
     = [E,B] + merger([object],[C,A,object],[C])
     = [E,B,C,A,object]
L[F] = [F] + merge(L[E],L[D],[E],[D])
     = [F] + merge([E,B,C,A,object],[D,A,object],[E],[D])
     = [F,E] + merge([B,C,A,object],[D,A,object],[D])
     = [F,E,B] + merge([C,A,object],[D,A,object],[D])
     = [F,E,B,C,D,A,object]
'''