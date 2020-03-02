#二分法

import math

#封装二次函数 方便调用 
def outer(a, b, c):
    def func(x):
        return a*x*x + b*x + c
    return func

#右偏移找f(a)*f(b)<0的点
def findX(x,y,f):
    i=0
    while f( x + math.exp(i)) * y > 0:
            i += 1
    return x + math.exp(i)

#二分求解  精度为p
def dich(a,b,p,f):
    m = (a+b)/2
    while (b-m) > p:
        if f(m) * f(a) > 0:
            a = m
        elif f(m) * f(a) == 0:
            return m, True
        else:
            b = m
        m = (a+b)/2
    return m, False










#输入系数
a = float(input("a = "))
while a == 0:
    print("a不能为0")
    a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))


#得到具体函数
f = outer(a, b, c)

#求驻点
y0 = 0
x0 = ( y0 - b ) / ( 2 * a)

#求极值点
x = x0
y0 = f(x)

#判断函数是否过x轴
if a * y0 < 0:
    #解的精度
    p = 10^-10
    x = findX(x, y0, f)
    r = dich(x0,x,p,f)

    #判断是否为近似解并输出
    if r[1]:
        print("解为："+str(r[0]) + ", " + str(2*x0 - r[0]) )
    else:
        print("近似解为："+str(r[0]) + ", " + str(2*x0 - r[0]) )


elif a * y0 == 0:
    print("解为：" + str(x0))

else:
    print("无解")



