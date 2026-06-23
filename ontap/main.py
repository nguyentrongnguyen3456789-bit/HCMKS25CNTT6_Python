class DeliveryOrder:
    def __init__(self, order_id, receiver_name, base_fee, distance, surcharge):
        self.order_id = order_id
        self.receiver_name = receiver_name
        self.base_fee = base_fee
        self.distance = distance
        self.surcharge = surcharge

        self.total_delivery_cost = 0
        self.delivery_status = ""

        self.calculate_total_cost()
        self.classify_delivery_status()

    def calculate_total_cost(self):
        self.total_delivery_cost = (self.base_fee * self.distance) + self.surcharge

    def classify_delivery_status(self):
        if self.total_delivery_cost < 100000:
            self.delivery_status = "Đơn hàng Tiêu chuẩn (Nội thành)"
        elif self.total_delivery_cost < 300000:
            self.delivery_status = "Đơn hàng Cận tỉnh"
        elif self.total_delivery_cost < 600000:
            self.delivery_status = "Đơn hàng Đường dài (Cần giám sát)"
        else:
            self.delivery_status = "Đơn hàng Đặc biệt (Ưu tiên cao - Rủi ro cao)"


class OrderManager:
    def __init__(self):
        self.orders = []

    def find_order(self, order_id):
        for order in self.orders:
            if order.order_id == order_id:
                return order
        return None

    def show_all_orders(self):
        if len(self.orders) == 0:
            print("Hệ thống chưa có vận đơn nào")
            return

        print("-" * 120)
        print(f"{'Mã Đơn':<15}{'Người Nhận':<25}{'Cước Nền':<15}"
              f"{'Khoảng Cách':<15}{'Phụ Phí':<15}"
              f"{'Tổng Chi Phí':<20}{'Trạng Thái'}")
        print("-" * 120)

        for order in self.orders:
            print(f"{order.order_id:<15}"
                  f"{order.receiver_name:<25}"
                  f"{order.base_fee:<15.0f}"
                  f"{order.distance:<15}"
                  f"{order.surcharge:<15.0f}"
                  f"{order.total_delivery_cost:<20.0f}"
                  f"{order.delivery_status}")

    def add_order(self):
        while True:
            order_id = input("Nhập mã vận đơn: ").strip()

            if order_id == "":
                print("Mã vận đơn không được để trống!")
                continue

            if self.find_order(order_id):
                print("Mã vận đơn đã tồn tại!")
                continue

            break

        while True:
            receiver_name = input("Nhập tên người nhận: ").strip()

            if receiver_name == "":
                print("Tên người nhận không được để trống!")
                continue

            break

        while True:
            try:
                base_fee = float(input("Nhập cước phí nền: "))
                if base_fee <= 0:
                    print("Cước phí phải lớn hơn 0!")
                    continue
                break
            except ValueError:
                print("Dữ liệu không hợp lệ!")

        while True:
            try:
                distance = int(input("Nhập khoảng cách (km): "))
                if distance < 1 or distance > 5000:
                    print("Khoảng cách phải từ 1 đến 5000 km!")
                    continue
                break
            except ValueError:
                print("Khoảng cách phải là số nguyên!")

        while True:
            try:
                surcharge = float(input("Nhập phụ phí: "))
                if surcharge <= 0:
                    print("Phụ phí phải lớn hơn 0!")
                    continue
                break
            except ValueError:
                print("Dữ liệu không hợp lệ!")

        order = DeliveryOrder(
            order_id,
            receiver_name,
            base_fee,
            distance,
            surcharge
        )

        self.orders.append(order)
        print("Thêm vận đơn thành công!")

    def update_order(self):
        order_id = input("Nhập mã vận đơn cần cập nhật: ")

        order = self.find_order(order_id)

        if not order:
            print("Không tìm thấy vận đơn!")
            return

        while True:
            try:
                base_fee = float(input("Nhập cước phí mới: "))
                if base_fee <= 0:
                    print("Cước phí phải lớn hơn 0!")
                    continue
                break
            except ValueError:
                print("Dữ liệu không hợp lệ!")

        while True:
            try:
                distance = int(input("Nhập khoảng cách mới: "))
                if distance < 1 or distance > 5000:
                    print("Khoảng cách phải từ 1 đến 5000!")
                    continue
                break
            except ValueError:
                print("Khoảng cách phải là số nguyên!")

        while True:
            try:
                surcharge = float(input("Nhập phụ phí mới: "))
                if surcharge <= 0:
                    print("Phụ phí phải lớn hơn 0!")
                    continue
                break
            except ValueError:
                print("Dữ liệu không hợp lệ!")

        order.base_fee = base_fee
        order.distance = distance
        order.surcharge = surcharge

        order.calculate_total_cost()
        order.classify_delivery_status()

        print("Cập nhật thành công!")

    def delete_order(self):
        order_id = input("Nhập mã vận đơn cần xóa: ")

        order = self.find_order(order_id)

        if not order:
            print("Không tìm thấy vận đơn!")
            return

        confirm = input(
            "Bạn có chắc muốn xóa vận đơn này khỏi hệ thống không? (Y/N): "
        )

        if confirm.lower() == "y":
            self.orders.remove(order)
            print("Xóa thành công!")
        else:
            print("Đã hủy thao tác!")

    def search_by_receiver(self):
        if len(self.orders) == 0:
            print("Hệ thống chưa có vận đơn nào")
            return

        keyword = input("Nhập tên người nhận cần tìm: ").lower()

        found = False

        for order in self.orders:
            if keyword in order.receiver_name.lower():
                print(
                    order.order_id,
                    order.receiver_name,
                    order.total_delivery_cost,
                    order.delivery_status
                )
                found = True

        if not found:
            print("Không tìm thấy vận đơn phù hợp")


def menu():
    print("\n================ MENU ================")
    print("1. Hiển thị danh sách vận đơn trong hệ thống")
    print("2. Nhập vận đơn mới")
    print("3. Cập nhật thông tin vận đơn")
    print("4. Xóa vận đơn khỏi hệ thống")
    print("5. Tìm kiếm vận đơn theo tên người nhận")
    print("6. Thoát")
    print("======================================")


def main():
    manager = OrderManager()

    while True:
        menu()

        choice = input("Nhập lựa chọn của bạn: ")

        match choice:
            case "1":
                manager.show_all_orders()

            case "2":
                manager.add_order()

            case "3":
                manager.update_order()

            case "4":
                manager.delete_order()

            case "5":
                manager.search_by_receiver()

            case "6":
                print("Cảm ơn bạn đã sử dụng hệ thống quản lý vận đơn!")
                break

            case _:
                print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()
