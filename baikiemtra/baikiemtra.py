def menu():
    print("=" * 60)
    print("1. Xem danh sách hàng tồn kho")
    print("2. Nhập thêm hàng hóa mới")
    print("3. Cập nhật số lượng tồn kho theo ID")
    print("4. Thoát chương trình")

inventory = [
    {'id': 'G01', 'name': 'Gạo tẻ', 'quantity': 50},
    {'id': 'G02', 'name': 'Mì tôm', 'quantity': 120}
]
def show_inventory(inventory_list):
    if not inventory_list:
        print("Kho hàng hiện đang trống!")
    else:
        print("{:<10} {:<20} {:<10}".format("ID", "Tên hàng hóa", "Số lượng"))
        print("-" * 40)
        for item in inventory_list:
            print("{:<10} {:<20} {:<10}".format(item['id'], item['name'], item['quantity']))

def add_item(inventory_list):
    while True:
        item_id = input("Nhập ID hàng hóa: ").strip()
        if item_id == "":
            print("ID không được để trống, vui lòng nhập lại!")
            continue
        break

    while True:
        item_name = input("Nhập tên hàng hóa: ").strip()
        if item_name == "":
            print("Tên hàng hóa không được để trống, vui lòng nhập lại!")
            continue
        break

    while True:
        try:
            quantity = int(input("Nhập số lượng: "))
            if quantity <= 0:
                print("Số lượng phải lớn hơn 0, vui lòng nhập lại!")
                continue
            break
        except ValueError:
            print("Số lượng phải là số nguyên, vui lòng nhập lại!")

    new_item = {'id': item_id, 'name': item_name, 'quantity': quantity}
    inventory_list.append(new_item)
    print("Thêm hàng hóa vào kho thành công!")

def update_quantity(inventory_list):
    item_id = input("Nhập ID hàng hóa cần cập nhật: ").strip()
    found = False
    for item in inventory_list:
        if item['id'] == item_id:
            found = True
            while True:
                try:
                    new_quantity = int(input("Nhập số lượng mới: "))
                    if new_quantity <= 0:
                        print("Số lượng phải lớn hơn 0, vui lòng nhập lại!")
                        continue
                    item['quantity'] = new_quantity
                    print("Cập nhật số lượng thành công!")
                    break
                except ValueError:
                    print("Số lượng phải là số nguyên, vui lòng nhập lại!")
            break
    if not found:
        print(f"Không tìm thấy hàng hóa có mã {item_id}!")
def main():
    while True:
        menu()
        choice = input("Nhập lựa chọn của bạn: ")
        match choice:
            case "1":
                show_inventory(inventory)
            case "2":
                add_item(inventory)
            case "3":
                update_quantity(inventory)
            case "4":
                print("Thoát chương trình")
                break
            case _:
                print("Lựa chọn không hợp lệ! Vui lòng nhập lại")

main()
