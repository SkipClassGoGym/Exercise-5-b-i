import math
n = int(input('Nhập căn bậc: ')) #2
m = int(input('Nhập số lần lặp: ')) #6
p = int(input('Nhập bậc của hàm loss: ')) #1
y = [100, 50, 20, 5.5, 1, 0.6]
y_hat = [99.5, 49.5, 19.5, 5, 0.5, 0.1]

def MD_nRE(n,m,p):
    loss = 0
    for i in range (1, m+1):
        loss +=round(math.pow(math.pow(y[i-1],1/n) - math.pow(y_hat[i-1],1/n),p),3)
    result =round((loss/m),4)
    return result

print(MD_nRE(n,m,p))