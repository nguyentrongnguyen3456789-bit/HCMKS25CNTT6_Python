bus_trips = []

def classify_status(available_seats, total_seats):

    if available_seats == 0:
        return "Hết vé"

    ratio = available_seats / total_seats

    if ratio < 0.15:
        return "Hút khách"

    elif ratio >= 0.15 and ratio <= 0.8:
        return "Bình thường"

    else:
        return "Ế khách"

def calculate_revenue(ticket_price, total_seats, available_seats):

    sold_seats = total_seats - available_seats

    return ticket_price * sold_seats

# TÌM CHUYẾN XE

def find_trip(trip_code):

    for trip in bus_trips:

        if trip["trip_code"].upper() == trip_code.upper():
            return trip

    return None

# HIỂN THỊ DANH SÁCH

def display_trips():

    if len(bus_trips) == 0:
        print("\nDanh sách chuyến xe đang trống!")
        return

    print("\n===================== DANH SÁCH CHUYẾN XE =====================")

    print(f"{'Mã CX':<10}"
          f"{'Tuyến đường':<30}"
          f"{'Giá vé':<15}"
          f"{'Ghế trống':<12}"
          f"{'Tổng ghế':<12}"
          f"{'Doanh thu':<15}"
          f"{'Trạng thái':<15}")

    for trip in bus_trips:

        print(f"{trip['trip_code']:<10}"
              f"{trip['route']:<30}"
              f"{trip['ticket_price']:<15}"
              f"{trip['available_seats']:<12}"
              f"{trip['total_seats']:<12}"
              f"{trip['revenue']:<15}"
              f"{trip['status']:<15}")


# THÊM CHUYẾN XE

def add_trip():

    while True:

        trip_code = input("Nhập mã chuyến xe: ").strip()

        if trip_code == "":
            print("Mã chuyến xe không được để trống!")
            continue

        if find_trip(trip_code):
            print("Mã chuyến xe đã tồn tại!")
            continue

        break

    while True:

        route = input("Nhập tuyến đường: ").strip()

        if route == "":
            print("Tuyến đường không được để trống!")
        else:
            break

    while True:

        try:
            ticket_price = int(input("Nhập giá vé: "))

            if ticket_price <= 0:
                print("Giá vé phải lớn hơn 0!")
            else:
                break

        except ValueError:
            print("Vui lòng nhập số hợp lệ!")

    while True:

        try:
            total_seats = int(input("Nhập tổng số ghế: "))

            if total_seats <= 0:
                print("Tổng số ghế phải lớn hơn 0!")
            else:
                break

        except ValueError:
            print("Vui lòng nhập số hợp lệ!")

    available_seats = total_seats

    trip = {
        "trip_code": trip_code,
        "route": route,
        "ticket_price": ticket_price,
        "available_seats": available_seats,
        "total_seats": total_seats,
        "revenue": 0,
        "status": classify_status(
            available_seats,
            total_seats
        )
    }

    bus_trips.append(trip)

    print("Thêm chuyến xe thành công!")

# ĐẶT VÉ

def book_ticket():

    if len(bus_trips) == 0:
        print("Danh sách chuyến xe đang trống!")
        return

    trip_code = input("Nhập mã chuyến xe: ").strip()

    if trip_code == "":
        print("Mã chuyến xe không được để trống!")
        return

    trip = find_trip(trip_code)

    if trip is None:
        print("Không tìm thấy chuyến xe!")
        return

    while True:

        try:
            quantity = int(input("Nhập số lượng vé đặt: "))

            if quantity <= 0:
                print("Số lượng vé phải lớn hơn 0!")

            elif quantity > trip["available_seats"]:
                print("Số vé vượt quá số ghế trống!")

            else:
                break

        except ValueError:
            print("Vui lòng nhập số nguyên!")

    trip["available_seats"] -= quantity

    trip["revenue"] = calculate_revenue(
        trip["ticket_price"],
        trip["total_seats"],
        trip["available_seats"]
    )

    trip["status"] = classify_status(
        trip["available_seats"],
        trip["total_seats"]
    )

    print("Đặt vé thành công!")

# XÓA CHUYẾN XE

def delete_trip():

    if len(bus_trips) == 0:
        print("Danh sách chuyến xe đang trống!")
        return

    trip_code = input("Nhập mã chuyến xe cần xóa: ").strip()
    if trip_code == "":
        print("Mã chuyến xe không được để trống!")
        return
    trip = find_trip(trip_code)

    if trip is None:
        print("Không tìm thấy chuyến xe!")
        return

    confirm = input(
        "Bạn có chắc muốn xóa chuyến xe này khỏi lịch trình không? (Y/N): "
    ).upper()

    if confirm == "Y":
        bus_trips.remove(trip)
        print("Xóa thành công!")
    else:
        print("Đã hủy thao tác xóa!")

# TÌM KIẾM

def search_trip():

    if len(bus_trips) == 0:
        print("Danh sách chuyến xe đang trống!")
        return

    print("\n1. Tìm theo mã chuyến xe")
    print("2. Tìm theo tuyến đường")

    choice = input("Chọn chức năng: ")

    results = []

    match choice:

        case "1":

            trip_code = input(
                "Nhập mã chuyến xe cần tìm: "
            ).strip()

            if trip_code == "":
                print("Mã chuyến xe không được để trống!")
                return

            for trip in bus_trips:

                if trip["trip_code"].upper() == trip_code.upper():
                    results.append(trip)

        case "2":

            keyword = input(
                "Nhập từ khóa tuyến đường: "
            ).strip().lower()

            if keyword == "":
                print("Từ khóa không được để trống!")
                return

            for trip in bus_trips:

                if keyword in trip["route"].lower():
                    results.append(trip)

        case _:
            print("Lựa chọn không hợp lệ!")
            return

    if len(results) == 0:
        print("Không tìm thấy dữ liệu!")
        return

    print(f"\n{'Mã CX':<10}"
          f"{'Tuyến đường':<30}"
          f"{'Giá vé':<15}"
          f"{'Ghế trống':<12}"
          f"{'Tổng ghế':<12}"
          f"{'Doanh thu':<15}"
          f"{'Trạng thái':<15}")

    for trip in results:

        print(f"{trip['trip_code']:<10}"
              f"{trip['route']:<30}"
              f"{trip['ticket_price']:<15}"
              f"{trip['available_seats']:<12}"
              f"{trip['total_seats']:<12}"
              f"{trip['revenue']:<15}"
              f"{trip['status']:<15}")


# THỐNG KÊ

def statistics():

    if len(bus_trips) == 0:
        print("Danh sách chuyến xe đang trống!")
        return

    sold_out = 0
    popular = 0
    normal = 0
    unpopular = 0

    for trip in bus_trips:

        match trip["status"]:

            case "Hết vé":
                sold_out += 1

            case "Hút khách":
                popular += 1

            case "Bình thường":
                normal += 1

            case "Ế khách":
                unpopular += 1

    print("\n========== THỐNG KÊ ==========")
    print("Hết vé      :", sold_out)
    print("Hút khách   :", popular)
    print("Bình thường :", normal)
    print("Ế khách     :", unpopular)

def refresh_data():

    if len(bus_trips) == 0:
        print("Danh sách chuyến xe đang trống!")
        return

    for trip in bus_trips:

        trip["revenue"] = calculate_revenue(
            trip["ticket_price"],
            trip["total_seats"],
            trip["available_seats"]
        )

        trip["status"] = classify_status(
            trip["available_seats"],
            trip["total_seats"]
        )

    print("Đã cập nhật toàn bộ dữ liệu thành công!")

def menu():

    print("\n========== HỆ THỐNG QUẢN LÝ CHUYẾN XE ==========")
    print("1. Hiển thị danh sách chuyến xe")
    print("2. Thêm chuyến xe mới")
    print("3. Cập nhật đặt vé")
    print("4. Hủy chuyến xe khỏi lịch trình")
    print("5. Tìm kiếm chuyến xe")
    print("6. Thống kê trạng thái chuyến xe")
    print("7. Phân loại trạng thái tự động")
    print("8. Thoát chương trình")

while True:
    menu()
    choice = input("Nhập lựa chọn: ")
    match choice:
        case "1":
            display_trips()
        case "2":
            add_trip()
        case "3":
            book_ticket()
        case "4":
            delete_trip()
        case "5":
            search_trip()
        case "6":
            statistics()
        case "7":
            refresh_data()
        case "8":
            print("Cảm ơn bạn đã sử dụng chương trình!")
            break
        case _:
            print("Lựa chọn không hợp lệ!")