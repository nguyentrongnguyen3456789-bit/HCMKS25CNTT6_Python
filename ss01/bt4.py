print("-- Tiếp nhận và chuẩn hóa sinh liệu")
patient_code = input("Nhập mã bệnh nhân ( ví dụ BN999) : ")
body_temperature = float(input(" Nhập nhiệt độ cơ thể : "))
heartbeat = int(input("nhập nhịp tim :"))

print("-- KẾT QUẢ CHUẨN HÓA DỮ LIỆU--")
print("Mã bệnh nhân",patient_code)
print("Nhiệt độ cơ thể: ",body_temperature,"độ c")
print("kiểu dữ liệu hệ thống ghi nhận:",type(body_temperature))
print("nhịp tim: ",heartbeat,"nhịp/phút")
print("kiểu dữ liệu hệ thống ghi nhận:",type(heartbeat))
print("----------------------------------")
print("Thông báo: DỮ liệu hợp lệ. Màn hình Monitor đã sẵn sàng kết nối!")

# Phân tích Input/Output
# Dữ liệu nhập từ bàn phím bằng input() thì ban đầu đều là chuỗi.
# Nhưng yêu cầu của đề là:
# Mã bệnh nhân: giữ nguyên chuỗi.
# Nhiệt độ cơ thể: cần chuyển sang float.
# Nhịp tim: cần chuyển sang int.
# Đầu ra mong muốn: hiển thị thông tin bệnh nhân kèm theo kiểu dữ liệu đã chuẩn hóa.

# Đề xuất giải pháp ép kiểu
# Giải pháp 1: Ép kiểu trực tiếp khi nhập. Ví dụ:
# body_temperature = float(input("Nhập nhiệt độ: "))
#  heartbeat = int(input("Nhập nhịp tim: "))
# Giải pháp 2: Nhập chuỗi trước, sau đó mới ép kiểu. Ví dụ:
# body_temperature_str = input("Nhập nhiệt độ: ")
# body_temperature = float(body_temperature_str)
# heartbeat_str = input("Nhập nhịp tim: ")
# heartbeat = int(heartbeat_str)
# Bảng so sánh
# Tiêu chí	Giải pháp 1: Ép trực tiếp	Giải pháp 2: Ép sau khi nhập
# Số lượng biến	Ít biến hơn	Nhiều biến hơn (có biến trung gian)
# Độ ngắn gọn của code	Ngắn gọn, dễ đọc	Dài hơn một chút
# Dễ debug (dò lỗi)	Khó tách riêng lỗi nhập và lỗi ép kiểu	Dễ kiểm tra từng bước hơn


# Chốt lựa chọn
# Trong môi trường bệnh viện, mình sẽ chọn giải pháp 2.
#  Vì tuy code dài hơn, nhưng dễ kiểm tra và xử lý lỗi nhập sai.
#  Dữ liệu bệnh nhân rất quan trọng, nên an toàn và dễ debug là ưu tiên hàng đầu.