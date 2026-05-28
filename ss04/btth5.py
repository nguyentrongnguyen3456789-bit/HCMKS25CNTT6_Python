total_revenue = 0
total_invoices = 0
large_invoices = 0

continue_input = "C"

while continue_input == "C" or continue_input == "c":
    invoice_value = int(input(f"Khách hàng {total_invoices + 1} - Nhập giá trị hóa đơn: "))

    total_revenue += invoice_value
    total_invoices += 1

    if invoice_value >= 1000000:
        large_invoices += 1

    continue_input = input("Có muốn nhập tiếp không? (C/K): ")
    print()

print("=== BÁO CÁO DOANH THU CUỐI NGÀY RIKKEI STORE ===")

print(f"Tổng số hóa đơn đã xử lý: {total_invoices} hóa đơn.")
print(f"Tổng doanh thu ngày hôm nay: {total_revenue:,} VND.")
print(f"Số hóa đơn lớn (>= 1,000,000 VND): {large_invoices} hóa đơn.")

if total_invoices > 0:
    percentage = (large_invoices / total_invoices) * 100
else:
    percentage = 0

print(f"Tỷ lệ hóa đơn lớn đạt: {percentage:.1f}% trên tổng số đơn hàng.")