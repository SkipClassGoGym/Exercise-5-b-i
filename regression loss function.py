import random
import math
n = int(input('Nhập số lần thử: '))

#Chọn hàm để tính
Loss_func = ['MAE', 'MSE', 'RMSE']

#Giả sử người dùng luôn nhập đúng

choose = str(input('Chọn hàm loss:\nMAE|MSE|RMSE\n')).strip().upper()
if choose == Loss_func[0]:
    loss1 = 0
    
    #Tính tổng hiệu của 2 biến target và predict
    for _ in range (1,n+1):
        target = random.uniform(0, 10)
        predict = random.uniform(0, 10)
        loss1 = loss1 + abs(target - predict)
        #print(f'Lần {_}\nTarget: {target}\nPredict: {predict}\n:Loss: {loss1}')
    MAE = loss1/n
    print (MAE)

else: 
    loss = 0 
    
    #Tổng của hiệu bình phương target và predict
    for _ in range (1,n+1):
        target = random.uniform(0, 10)
        predict = random.uniform(0, 10)
        loss = loss + (target - predict)**2
        #print(f'Lần {_}\nTarget: {target}\nPredict: {predict}\n:Loss: {loss}')
    
    #Tính MSE
    if choose == Loss_func[1]:
        MSE = loss/n
        print(MSE)
    
    #Tính RMSE
    elif choose == Loss_func[2]:
        RMSE = math.sqrt(loss/n)
        print(RMSE)

        