def compute_interest(money, period):
    daily_rate = 1 + 1 / 365  # Lãi suất nhận được mỗi ngày
    for _ in range(period):
        money = money*daily_rate  # Cập nhật số tiền mỗi ngày
    return round(money, 3)  # Trả về kết quả đã làm tròn đến 3 chữ số thập phân

# Ví dụ:
print(compute_interest(1, 12))   # Test case 1: 2.613
print(compute_interest(1, 365))  # Test case 2: 2.714
print(compute_interest(1, 730))  # Test case 3: 2.716
