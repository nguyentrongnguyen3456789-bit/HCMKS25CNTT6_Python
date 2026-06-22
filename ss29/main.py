class Product:
    def __init__(self, id, name, import_price,quantity, storage_fee):
        self.id = id
        self.name = name
        self.import_price = import_price
        self.quantity = quantity
        self.storage_fee = storage_fee
        self.total_value = ""
        self.stock_status = 0

        self.calculate_total_value()
        self.classify_stock_status()

    def calculate_total_value(self):
        self.total_value = (self.import_price * self.quantity) + self.storage_fee
    
    def classify_stock_status(self):
        if self.total_value < 9_000_000:
            self.stock_status = "Thấp (An toàn)"
        elif self.total_value < 15_000_000:
            self.stock_status = "Trung bình"
        elif self.total_value < 30_000_000:
            self.stock_status = "Cao (Cần chú ý)"
        else:
            self.stock_status = "Rất cao (Rủi ro ứ đọng vốn)"

class ProductManager:
    def __init__(self):
        self.products = []



def main():
    while True:
        print("\n============= MENU ==============")
        print("1. Hiển thị danh sách sản phẩm trong kho")
        print("2. Nhập sản phẩm mới vào kho")
        print("3. Cập nhật thông tin sản phẩm")
        print("4. Xóa sản phẩm khỏi kho")
        print("5. Tìm kiếm sản phẩm theo tên")
        print("6. Thoát")

        choice = input("Nhập lựa chọn của bạn: ")

        match choice:
            case "1":
                print("Hiển thị danh sách")

            case "2":
                print("Thêm sản phẩm")

            case "3":
                print("Cập nhật sản phẩm")

            case "4":
                print("Xóa sản phẩm")

            case "5":
                print("Tìm kiếm sản phẩm")

            case "6":
                print("Cảm ơn bạn đã sử dụng hệ thống quản lý kho hàng!")
                break

            case _:
                print("Lựa chọn không hợp lệ! Vui lòng nhập lại")


if __name__ == "__main__":
    main()
            





        

