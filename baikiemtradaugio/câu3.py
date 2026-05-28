ton_kho = 100
while True:
    quanity=int(input("nhập vào Số lượng muốn xuất: "))
    if quanity < 0:
        print("Không được nhập số âm, vui lòng nhập lại!")
    elif quanity > ton_kho:
        print("Kho không đủ hàng, vui lòng nhập lại!")
    else:
        ton_kho-=quanity
        break
print("Xuất kho thành công",ton_kho)