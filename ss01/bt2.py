print("--- HỆ THỐNG NHẬP CHỈ SỐ SINH TỒN---")
name_patient = input(" Nhập tên bệnh nhân : ")
weight =float(input(" Nhập cân nặng bệnh nhân : "))

print("---KIỂM TRA DỮ LIỆU LƯU TRƯC---")
print("Bệnh nhân :",name_patient)
print("Cân nặng đã nhập :",weight)

print("CẢNH BÁO - Kiểu dữ liệu đang lưu là : ", type(weight))
# input() trong Python lúc nào cũng coi dữ liệu nhập vào là chuỗi hết,
# cho dù mình gõ số hay chữ. Vì vậy khi mình nhập số,
# nó vẫn lưu thành chuỗi, không phải số thật.
# Muốn dùng để tính toán thì mình phải tự đổi sang kiểu số bằng int() hoặc float().