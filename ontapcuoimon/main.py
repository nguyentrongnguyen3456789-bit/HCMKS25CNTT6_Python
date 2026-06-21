class Student:
    def __init__(self, id, name, theory_score, practice_score, project_score):
        self.__id = id
        self.__name = name
        self.__theory_score = theory_score
        self.__practice_score = practice_score
        self.__project_score = project_score

        self.__final_score = 0
        self.__academic_rank = ""

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def theory_score(self):
        return self.__theory_score

    @property
    def practice_score(self):
        return self.__practice_score

    @property
    def project_score(self):
        return self.__project_score

    @property
    def final_score(self):
        return self.__final_score

    @property
    def academic_rank(self):
        return self.__academic_rank

    def update_theory_score(self, theory_score):
        self.__theory_score = theory_score

    def update_practice_score(self, practice_score):
        self.__practice_score = practice_score

    def update_project_score(self, project_score):
        self.__project_score = project_score

    def calculate_final_score(self):
        self.__final_score = (
            self.__theory_score * 0.2
            + self.__practice_score * 0.3
            + self.__project_score * 0.5
        )

    def classify_academic_rank(self):
        if self.__final_score < 5:
            self.__academic_rank = "Yếu"

        elif self.__final_score < 7:
            self.__academic_rank = "Trung bình"

        elif self.__final_score < 8.5:
            self.__academic_rank = "Khá"

        else:
            self.__academic_rank = "Giỏi"


class StudentManager:
    def __init__(self):
        self.students = []

    def input_student_id(self):
        while True:
            stu_id = input("Nhập mã sinh viên: ").strip()

            if not stu_id:
                print("Mã sinh viên không được để trống!")
                continue

            duplicate = False

            for stu in self.students:
                if stu.id.lower() == stu_id.lower():
                    duplicate = True
                    break

            if duplicate:
                print("Mã sinh viên đã tồn tại!")
            else:
                return stu_id

    def input_student_name(self):
        while True:
            name = input("Nhập họ tên sinh viên: ").strip()

            if not name:
                print("Họ tên không được để trống!")
            else:
                return name

    def input_score(self, message):
        while True:
            try:
                score = float(input(message))

                if 0 <= score <= 10:
                    return score

                print("Điểm phải nằm trong khoảng từ 0 đến 10!")

            except ValueError:
                print("Vui lòng nhập số hợp lệ!")

    def add_student(self):
        stu_id = self.input_student_id()

        stu_name = self.input_student_name()

        theory_score = self.input_score(
            "Nhập điểm lý thuyết: "
        )

        practice_score = self.input_score(
            "Nhập điểm thực hành: "
        )

        project_score = self.input_score(
            "Nhập điểm đồ án: "
        )

        student = Student(
            stu_id,
            stu_name,
            theory_score,
            practice_score,
            project_score
        )

        student.calculate_final_score()
        student.classify_academic_rank()

        self.students.append(student)

        print("Thêm sinh viên thành công!")

    def show_all(self):
        if not self.students:
            print("Danh sách sinh viên trống!")
            return

        print("-" * 120)

        print(
            f"{'Mã SV':<10}"
            f"{'Họ tên':<25}"
            f"{'Lý thuyết':<15}"
            f"{'Thực hành':<15}"
            f"{'Đồ án':<15}"
            f"{'Tổng kết':<15}"
            f"{'Học lực':<15}"
        )

        print("-" * 120)

        for stu in self.students:
            print(
                f"{stu.id:<10}"
                f"{stu.name:<25}"
                f"{stu.theory_score:<15.1f}"
                f"{stu.practice_score:<15.1f}"
                f"{stu.project_score:<15.1f}"
                f"{stu.final_score:<15.2f}"
                f"{stu.academic_rank:<15}"
            )

    def update_student(self):
        stu_id = input(
            "Nhập mã sinh viên cần cập nhật: "
        ).strip()

        for stu in self.students:

            if stu.id.lower() == stu_id.lower():

                theory_score = self.input_score(
                    "Nhập điểm lý thuyết mới: "
                )

                practice_score = self.input_score(
                    "Nhập điểm thực hành mới: "
                )

                project_score = self.input_score(
                    "Nhập điểm đồ án mới: "
                )

                stu.update_theory_score(theory_score)
                stu.update_practice_score(practice_score)
                stu.update_project_score(project_score)

                stu.calculate_final_score()
                stu.classify_academic_rank()

                print("Cập nhật thành công!")

                return

        print("Không tìm thấy sinh viên!")

    def delete_student(self):
        stu_id = input(
            "Nhập mã sinh viên cần xóa: "
        ).strip()

        for stu in self.students:

            if stu.id.lower() == stu_id.lower():

                while True:

                    choice = input(
                        "Bạn có chắc muốn xóa sinh viên này không? (Y/N): "
                    ).strip().lower()

                    if choice == "y":

                        self.students.remove(stu)

                        print("Xóa sinh viên thành công!")

                        return

                    elif choice == "n":

                        print("Đã hủy thao tác xóa!")

                        return

                    else:

                        print("Vui lòng nhập Y hoặc N!")

        print("Không tìm thấy sinh viên!")

    def search_student(self):
        keyword = input(
            "Nhập tên sinh viên cần tìm: "
        ).strip().lower()

        if not keyword:
            print("Từ khóa tìm kiếm không được để trống!")
            return

        found = False

        print("-" * 120)

        print(
            f"{'Mã SV':<10}"
            f"{'Họ tên':<25}"
            f"{'Lý thuyết':<15}"
            f"{'Thực hành':<15}"
            f"{'Đồ án':<15}"
            f"{'Tổng kết':<15}"
            f"{'Học lực':<15}"
        )

        print("-" * 120)

        for stu in self.students:

            if keyword in stu.name.lower():

                print(
                    f"{stu.id:<10}"
                    f"{stu.name:<25}"
                    f"{stu.theory_score:<15.1f}"
                    f"{stu.practice_score:<15.1f}"
                    f"{stu.project_score:<15.1f}"
                    f"{stu.final_score:<15.2f}"
                    f"{stu.academic_rank:<15}"
                )

                found = True

        if not found:
            print("Không tìm thấy sinh viên phù hợp")


def main():
    manager = StudentManager()

    while True:

        print("\n================ MENU ================")
        print("1. Hiển thị danh sách sinh viên")
        print("2. Thêm sinh viên mới")
        print("3. Cập nhật thông tin sinh viên")
        print("4. Xóa sinh viên")
        print("5. Tìm kiếm sinh viên theo tên")
        print("6. Thoát")
        print("=====================================")

        try:

            choice = int(
                input("Nhập lựa chọn của bạn: ")
            )

            match choice:

                case 1:
                    manager.show_all()

                case 2:
                    manager.add_student()

                case 3:
                    manager.update_student()

                case 4:
                    manager.delete_student()

                case 5:
                    manager.search_student()

                case 6:
                    print(
                        "Cảm ơn bạn đã sử dụng hệ thống quản lý học tập!"
                    )
                    break

                case _:
                    print("Lựa chọn không hợp lệ!")

        except ValueError:
            print("Vui lòng nhập số từ 1 đến 6!")


if __name__ == "__main__":
    main()

