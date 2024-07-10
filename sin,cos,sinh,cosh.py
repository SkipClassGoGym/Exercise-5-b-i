import math
x = float(input('Nhập x: '))
n = int(input('Nhập số lần tính xấp xỉ: '))
#Tính giai thừa cho hàm sin và sinh 
def factorial(i):
    m = 2*i + 1
    giaithua = 1
    for r in range (1, m + 1):
        giaithua *= r 
    return giaithua

def sin(x):
    sin_x = 0
    for i in range (0, n +1):
        sin_x += math.pow(-1,i)*(math.pow(x,(2*i+1))/(factorial(i)))
    return sin_x

def sinh(x):
    sinh_x = 0
    for i in range (0, n +1):
        sinh_x += (math.pow(x,(2*i+1))/(factorial(i)))
    return sinh_x
#Tính giai thừa cho hàm cos và cosh
def factorial1(i):
    m = 2*i 
    giaithua = 1
    for r in range (1, m + 1):
        giaithua *= r 
    return giaithua

def cos(x):
    cos_x = 0
    for i in range (0, n +1):
        cos_x += math.pow(-1,i)*(math.pow(x,(2*i))/(factorial1(i)))
    return cos_x

def cosh(x):
    cosh_x = 0
    for i in range (0, n +1):
        cosh_x += (math.pow(x,(2*i))/(factorial1(i)))
    return cosh_x

print (f' Sin(x): {sin(x)}')
print (f'Cos(x): {cos(x)}')
print (f'Sinh(x): {sinh(x)}')
print (f'Cosh(x): {cosh(x)}')
