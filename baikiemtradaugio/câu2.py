Total_defective_items = 0
total = 0
while True:
    quanity =int(input("nhập số lượng hàng lỗi của từng quầy: "))
    if quanity <= 0:
        print("Đã thống kê xong")
        break
    else:
        total+=quanity
print("Tổng số hàng lỗi thu hồi trong ngày là: ",total)