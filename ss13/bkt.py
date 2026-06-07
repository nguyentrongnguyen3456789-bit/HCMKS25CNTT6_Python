employees = []
next_id = 101

while True:
    print("----- QUẢN LÝ NHÂN SỰ - STAFF MANAGER-----\n"
          "1. Thêm nhân viên mới\n"
          "2. Danh sách nhân viên\n"
          "3. Xóa nhân viên khỏi hệ thống\n"
          "4. Thoát chương trình\n"
          )
    choice = input("Nhập chức năng bạn muốn: ")
    match choice:
        case "1":
            while True:
                name = input("Nhập tên nhân viên: ").strip()
                if name != "":
                    break
                else:
                    print("Tên nhân viên không được để trống!")

            while True:
                salary = input("Nhập mức lương: ").strip()
                if salary.isdigit() and int(salary) > 0:
                    salary = int(salary)
                    break
                print("Mức lương phải là số dương lớn hơn 0!")

            employees.append([next_id, name, salary])
            print(f"Thêm nhân viên thành công! ID: {next_id}")
            next_id += 1

        case "2":
            if len(employees) == 0:
                print("Chưa có dữ liệu nhân sự!")
            else:
                print("ID | TÊN NHÂN VIÊN | MỨC LƯƠNG")
                print("--------------------------------")
                for employee in employees:
                    print(f"{employee[0]} | {employee[1]} | {employee[2]}")

        case "3":
            delete_id = input("Nhập ID nhân viên cần xóa: ")
            found = False
            for employee in employees:
                if str(employee[0]) == delete_id:
                    employees.remove(employee)
                    found = True
                    print(f"Đã xóa nhân viên ID {delete_id} thành công!")
                    break
            if not found:
                print("Không tìm thấy nhân viên để xóa!")

        case "4":
            print("Thoát chương trình!")
            break

        case _:
            print("Lựa chọn không hợp lệ!")
