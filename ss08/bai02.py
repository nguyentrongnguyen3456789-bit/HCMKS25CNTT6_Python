
shop_name = ""
product_name = ""
description = ""
category = ""
keywords = []
voucher_list = []

while True:

    print("\n+============================================================+")
    print("|    HỆ THỐNG QUẢN LÝ NỘI DUNG SẢN PHẨM SHOPEE              |")
    print("+============================================================+")
    print("|    1. Nhập dữ liệu sản phẩm và xem báo cáo thống kê        |")
    print("|    2. Chuẩn hóa tên shop                                  |")
    print("|    3. Kiểm tra mã giảm giá hợp lệ                         |")
    print("|    4. Tìm kiếm và thay thế từ khóa trong mô tả sản phẩm   |")
    print("|    5. Thoát chương trình                                  |")
    print("+============================================================+")

    choice = input("> Mời bạn chọn chức năng (1-5): ").strip()

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ")
        continue


    if choice not in ["1", "2", "3", "4", "5"]:
        print("Lựa chọn không hợp lệ")
        continue

    match choice:

        # CHỨC NĂNG 1
    
        case "1":

            shop_name = input("Nhập tên shop: ")
            product_name = input("Nhập tên sản phẩm: ")
            description = input("Nhập mô tả sản phẩm: ")
            category = input("Nhập danh mục sản phẩm: ")
            keyword_input = input(
                "Nhập danh sách từ khóa tìm kiếm (cách nhau bởi dấu phẩy): "
            )

            
            if shop_name.strip() == "":
                print("Tên shop không được bỏ trống")
                continue

           
            if description.strip() == "":
                print("Mô tả sản phẩm không được rỗng")
                continue

            
            shop_name = shop_name.strip()
            product_name = product_name.strip().title()
            description = description.strip()

            category = " ".join(category.split()).lower()

            keywords = []
            for word in keyword_input.split(","):
                word = word.strip()

                if word != "":
                    keywords.append(word)

            
            print("\n===== BÁO CÁO THỐNG KÊ =====")

            print(f"Tên shop: {shop_name}")
            print(f"Tên sản phẩm: {product_name}")
            print(f"Mô tả sản phẩm: {description}")

            print(f"Độ dài mô tả sản phẩm: {len(description)}")

            print(f"Danh mục sản phẩm: {category}")

            print(
                f"Danh sách từ khóa: {', '.join(keywords)}"
            )

            print(
                f"Số lượng từ khóa tìm kiếm: {len(keywords)}"
            )

            print(
                f"Mô tả chuyển sang chữ thường: {description.lower()}"
            )

            print(
                f"Mô tả chuyển sang chữ hoa: {description.upper()}"
            )

        # CHỨC NĂNG 2
 
        case "2":

            if shop_name == "":
                print("Vui lòng nhập dữ liệu sản phẩm ở chức năng 1 trước!")
                continue

            print("\n===== CHUẨN HÓA TÊN SHOP =====")

            print(f"Tên shop ban đầu: {shop_name}")

            normalized_shop = "-".join(
                shop_name.strip().lower().split()
            )

            if not normalized_shop.startswith("shop-"):
                normalized_shop = "shop-" + normalized_shop

            print(f"Tên shop sau chuẩn hóa: {normalized_shop}")


        # CHỨC NĂNG 3

        case "3":

            if shop_name == "":
                print("Vui lòng nhập dữ liệu sản phẩm ở chức năng 1 trước!")
                continue

            voucher = input("Nhập mã giảm giá: ").strip()

            if voucher == "":
                print("Mã giảm giá không được rỗng")

            elif " " in voucher:
                print("Mã giảm giá không được chứa khoảng trắng")

            elif len(voucher) < 6 or len(voucher) > 12:
                print("Mã giảm giá phải có độ dài từ 6 đến 12 ký tự")

            elif not voucher.isupper():
                print("Mã giảm giá phải được viết hoa toàn bộ")

            elif not voucher.isalnum():
                print("Mã giảm giá chỉ được chứa chữ cái và chữ số")

            elif not voucher.startswith("SALE"):
                print("Mã giảm giá phải bắt đầu bằng chuỗi SALE")

            else:
                print("Mã giảm giá hợp lệ")

                voucher_list.append(voucher)

                print(
                    f"Danh sách mã giảm giá hiện tại: {', '.join(voucher_list)}"
                )

        # CHỨC NĂNG 4
        case "4":

            if description == "":
                print("Vui lòng nhập dữ liệu sản phẩm ở chức năng 1 trước!")
                continue

            find_word = input("Nhập từ khóa cần tìm: ").strip()

            if find_word == "":
                print("Từ khóa cần tìm không được rỗng")
                continue

            replace_word = input("Nhập từ khóa thay thế: ")

            if find_word in description:

                count_word = description.count(find_word)

                description = description.replace(
                    find_word,
                    replace_word
                )

                print(
                    f"Số lần xuất hiện của từ khóa: {count_word}"
                )

                print("Mô tả sau khi thay thế:")
                print(description)

            else:
                print(
                    "Không tìm thấy từ khóa trong mô tả sản phẩm"
                )

        # CHỨC NĂNG 5
        case "5":

            print("Thoát chương trình")
            break
