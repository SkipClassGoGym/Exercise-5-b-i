a = float(input("Nhập số tự nhiên a: "))
while a < 0:
    a = float(input('Nhập lại số tự nhiên a: '))
xo = a
EPISILON = 0.001

if a ==0:
    print (a)
else:
    #Công thức tính nhị thức
    while True:
        #tính x_n1
        x_n1 = xo - ((xo*xo-a)/(2*xo))
        if abs(x_n1 - xo) < EPISILON:
            print(x_n1)
            break
        else:
            xo= x_n1