# name = input ('nhập tên của bạn:')
# print("hello cậu nha",name)

# quy tắc đặt tên biến
# không bắt đầu bằng số
# không chứa khoảng trắng
# không được chứa các Ký tự đặc biệt
#  là những ký hiệu ngoài
# chữ cái,số,dấu gạch dưới _
# phân biệt chữ hoa và thường

# cách 1: ép kiểu dữ liệu từ chuỗi sang số (str -> int)
#year_of_birth = int(input("hãy nhập tuổi của bạn:"))
# print("tuổi của tôi sau 10 năm nữa là:",year_of_birth + 10)

# cách 2
# year_of_birth = int(input("Hãy nhập tuổi của bạn: "))
# print(f"Tuổi của tôi sau 10 năm nữa: {year_of_birth + 10}")
 
# yêu cầu : cho người dùng nhập vào năm sinh và tính ra số tuổi sau 7 năm
year_of_birth = int(input("Hãy nhập vào năm sinh của bạn: "))
age = 2026 - year_of_birth + 7
print(f"Tuổi của bạn sau 7 năm nữa là:",age)