# cho phép thu ngân nhập vào tổng số tiền ban đầu của hóa đơn( số nguyên )
total_invoice = int(input("nhập tổng tiền hóa đơn ban đầu :"))

# nếu hóa đơn từ 500,000 VND trở lên: giảm 10% trên tổng số tiền đó.
if(total_invoice >= 500000):
    discount_price = total_invoice * 0.1
    total_invoice *= 0.9

print("--HÓA ĐƠN THANH TOÁN RIKKEI STORE---")
print("tổng tiền khách hàng phải trả: ",total_invoice)
print("số tiền được giảm giá: ",discount_price)