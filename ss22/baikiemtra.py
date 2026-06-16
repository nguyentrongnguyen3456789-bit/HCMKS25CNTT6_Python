def show_devices(devices):
    if not devices:
        print("Danh sách rỗng")
        return
    print("== Danh sách thiết bị giám sát ==")
    print(f"{'MÃ TB':<5} - {'Vị trí phân xường':<25} {'Chỉ số cũ':<15} {'Chỉ số mới':<15} {'Trạng Thái':<20} ")
    for item in devices:
        print(f"{item.get('id'):<5} - {item.get('location'):<25} {item.get('Old index'):<15} {item.get('id'):<15} {item.get('id'):<20} ")
def main():
    devices = [
    {'id': 'M01', 'location': 'Mechanical Shop A', 'old_index': 1200, 'new_index': 4500, 'status': 'Normal'},
    {'id': 'M02', 'location': 'Assembly Line B', 'old_index': 2300, 'new_index': 8500, 'status': 'Overload'}
]
    print("======= SMART ENERGY MONITOR - PHÒNG CƠ ĐIỆN =======\n")
    print("1. Xem danh sách thiết bị giám sát\n")
    print("2. Cập nhật chỉ số điện tiêu thụ (check-in)\n")
    print("3. Kích hoạt trạng thái cảnh báo quá tải\n")
    print("4. Tính tổng lương điện và Chi phí năng lương\n")
    print("5. Thoát chương trình")

    choice = input("Nhập lựa chọn của bạn :")

    match choice:
        case "5":
            print("Thoát chương trình!")
            return
        case _:
            print("Lựa chọn không hợp lệ")

if __name__ == "__main__":
    main()