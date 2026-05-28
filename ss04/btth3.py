total_invoice = int(input("nhập số lượng hóa đơn trong ca: "))
max = None
min = None
for i in range(1,total_invoice + 1):
   value_invoice = float(input(f"nhập giá trị hóa đơn thứ {i}: "))
   if(max is None or value_invoice > max):
      max = value_invoice
   if(min is None or value_invoice < min):
      min = value_invoice
print(f"Hóa đơn có giá trị cao nhất : {max}")
print(f"Hóa đơn có giá trị nhỏ nhất : {min}")
