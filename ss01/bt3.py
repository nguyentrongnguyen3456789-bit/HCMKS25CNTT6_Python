print("---- HỆ THỐNG TIẾP NHẬN BỆNH NHÂN ----")
name_patient = input("Nhập họ và tên bệnh nhân: ")
medical_code = input("Nhập mã bệnh án (ví dụ: BN1024): ")
department = input("Nhập khoa/phòng khám chỉ định: ")
print("---- PHIẾU KHÁM BỆNH ----")
print(f"Bệnh nhân: {name_patient} - Mã BA: {medical_code} - Chuyển tới: {department}")

# Phân tích:  
# Bài yêu cầu nhập ba thông tin: họ tên bệnh nhân, mã bệnh án, và khoa/phòng khám.
#  Tất cả đều là chữ nên mình sẽ dùng input() để lấy dữ liệu.
#  Sau đó, chương trình cần in ra một dòng phiếu khám bệnh điện tử theo đúng mẫu.

# Giải pháp:  
# Cách làm khá đơn giản: mình cho chương trình hiện tiêu đề,
#  rồi lần lượt hỏi người dùng nhập ba thông tin.
#  Cuối cùng, mình dùng print() kết hợp f-string để hiển thị lại phiếu khám bệnh với dữ liệu vừa nhập