import math

while True:
    try:
        x = float(input('Nhập x: '))
        break
    except ValueError:
        print('Giá trị nhập vào không hợp lệ. Xin vui lòng nhập một số thực.')

activate_func =['sigmoid','relu','elu']
#Chon activate_func
print('Xin vui lòng chọn 1 trong 3 activate function: \nsigmoid| relu| elu')
choose = str(input('Chọn activate function: ')).strip().lower()
while choose not in activate_func:
    print(f'{choose} is not supported')
    print('Xin vui lòng chọn 1 trong 3 activate function: \nsigmoid| relu| elu')
    choose = str(input('Chọn activate function: ')).strip().lower()

if choose==activate_func[0]:
    
    sigmoid = 1/(1+math.e**(-x))
    print (sigmoid)

elif choose==activate_func[1]:

    if x <= 0:
        relu = 0
    if x > 0:
        relu = x
    print(relu)

elif choose==activate_func[2]:
    
    if x <=0:
        alpha = float(input('Nhập hệ số alpha: '))
        elu = alpha*(math.e - 1)
    elif x > 0:
        elu = x
    
    print (elu)



