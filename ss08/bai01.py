
account_name = ""
title = ""
description = ""
hashtags = []

while True:
    print("\n+================================================+")
    print("|    HỆ THỐNG QUẢN LÝ NỘI DUNG TIKTOK           |")
    print("+================================================+")
    print("|    1. Nhập và phân tích thông tin video        |")
    print("|    2. Chuẩn hóa tên tài khoản                  |")
    print("|    3. Kiểm tra tính hợp lệ hashtag             |")
    print("|    4. Tìm kiếm và thay thế từ khóa trong mô tả |")
    print("|    5. Thoát chương trình                       |")
    print("+================================================+")

    choice = input("> Mời bạn chọn chức năng (1-5): ").strip()

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ!")
        continue

    match choice:

  
        case "1":

            account_name = input("Nhập tên tài khoản: ")
            title = input("Nhập tiêu đề video: ")
            description = input("Nhập mô tả video: ")
            hashtag_input = input("Nhập danh sách hashtag (cách nhau bằng dấu phẩy): ")

            if account_name.strip() == "":
                print("Tên tài khoản không được rỗng")
                continue

            if description.strip() == "":
                print("Mô tả video không được rỗng")
                continue

            account_name = account_name.strip()
            title = title.strip().title()
            description = description.strip()

            hashtags = []
            for tag in hashtag_input.split(","):
                tag = tag.strip()
                if tag != "":
                    hashtags.append(tag)

            print("\n===== BÁO CÁO THỐNG KÊ =====")

            print(f"Tên tài khoản: {account_name}")
            print(f"Tiêu đề: {title}")
            print(f"Mô tả: {description}")

            print(f"Độ dài mô tả video: {len(description)}")

            word_count = len(description.split())
            print(f"Số lượng từ trong mô tả: {word_count}")

            print(f"Danh sách hashtag sau chuẩn hóa: {', '.join(hashtags)}")

            print(f"Số lượng hashtag: {len(hashtags)}")

            print(f"Mô tả chữ thường: {description.lower()}")

            print(f"Mô tả chữ hoa: {description.upper()}")


        case "2":

            if account_name == "":
                print("Vui lòng nhập dữ liệu video ở chức năng 1 trước!")
                continue

            print("\n===== CHUẨN HÓA TÀI KHOẢN =====")
            print(f"Tên tài khoản ban đầu: {account_name}")

            normalized_account = "@" + account_name.lower()

            print(f"Tên tài khoản chuẩn hóa: {normalized_account}")

        case "3":

            if account_name == "":
                print("Vui lòng nhập dữ liệu video ở chức năng 1 trước!")
                continue

            new_hashtag = input("Nhập hashtag mới: ").strip()

            if new_hashtag == "":
                print("Hashtag không được rỗng")

            elif not new_hashtag.startswith("#"):
                print("Hashtag phải bắt đầu bằng ký tự #")

            elif " " in new_hashtag:
                print("Hashtag không được chứa khoảng trắng")

            elif len(new_hashtag) < 2:
                print("Hashtag phải có ít nhất 2 ký tự")

            else:

                hashtag_content = new_hashtag[1:]

                if not hashtag_content.replace("_", "").isalnum():
                    print("Hashtag chỉ được chứa chữ cái, chữ số hoặc dấu gạch dưới")

                else:
                    print("Hashtag hợp lệ")

                    hashtags.append(new_hashtag)

                    print("Danh sách hashtag hiện tại:")
                    print(", ".join(hashtags))


        case "4":

            if description == "":
                print("Vui lòng nhập dữ liệu video ở chức năng 1 trước!")
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

                print(f"Mô tả sau khi thay thế: {description}")

                print(f"Số lần xuất hiện của từ khóa: {count_word}")

            else:
                print("Không tìm thấy từ khóa trong mô tả")
        case "5":
            print("Thoát chương trình")
            break
        case _:
            print("Lựa chọn không hợp lệ!")
