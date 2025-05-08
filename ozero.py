#Deros.All rights reserved
#=========================
from scipy.integrate import quad
from numpy import sin, tan

def d1(x):
    return sin(x)
def d2(x):
    return x ** 2
def d3(x):
    return x ** 3
def d4(x):
    return tan(x)
def s(x1, x2, d):
    res = quad(d, x2, x1)[0]
    return res



def avt():
    a = int(input('Дайте денег: \n'))
    if a >= 10 and a <30:
        print(s(2, 0, d1))
        print('Жетон №1')
    elif a >= 30 and a < 50:
        print(s(3, 2, d2) + s(3, 1, d3))
        print('Жетон №2')
    elif a >= 50:
        print(s(4, -2, d4))
        print('Жетон №3')
    else:
        print("нищий бомж, воняй")
avt()
    

