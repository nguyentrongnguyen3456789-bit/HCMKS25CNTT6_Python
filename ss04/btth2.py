# sử dụng vòng lặp chạy đúng 7 lần để yêu cầu người
# người dùng nhập vào doanh thu của từng ngày( in ra thông báo từ ngày 1 đến 7)
total_revenue = 0
count = 0
for i in range(1,8):
    revenue =int(input(f"nhập doanh thu ngày {i}: "))
    if(revenue >= 5000000):
        count+=1
    total_revenue += revenue

avg_revenue = total_revenue / 7
print(f"Tổng doanh thu cả tuần: {total_revenue}")
print(f"Doanh thu trung bình mỗi ngày: {avg_revenue:.2f}")
print(f"Số ngày đạt doanh thu mục tiêu (>=5,000,000 VND): {count} ngày")