quanity = int(input("Nhập số lượng tồn kho: "))
if (quanity >= 50):
    print("Tình trạng: Hàng đầy kho")
elif 10 <= quanity and quanity < 50:
    print("Tình trạng: Mức an toàn")
else:
    print("Tình trạng: Sắp hết hàng, cần báo cáo nhập thêm")