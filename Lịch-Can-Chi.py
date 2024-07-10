print('Chào mừng bạn đến với chương trình tính lịch Can Chi')
year = int(input('Nhập năm sinh: '))
# Người thông minh luôn nhập số nguyên dương
tinhcan = {
    0: 'Canh', 
    1: 'Tân', 
    2: 'Nhâm', 
    3: 'Quý', 
    4: 'Giáp',
    5: 'Ất', 
    6: 'Bính', 
    7: 'Đinh', 
    8: 'Mậu', 
    9: 'Kỷ'
}
tinhchi = {
    0: 'Thân', 
    1: 'Dậu', 
    2: 'Tuất', 
    3: 'Hợi', 
    4: 'Tý', 
    5: 'Sửu', 
    6: 'Dần', 
    7: 'Mão', 
    8: 'Thìn', 
    9: 'Tỵ', 
    10: 'Ngọ', 
    11: 'Mùi'
}
can = year % 10
chi = year % 12
print (tinhcan[can],tinhchi[chi])