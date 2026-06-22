from abc import ABC, abstractmethod
class BaseCharacter(ABC):
    def __init__(self, hp):
        self.__base_hp = hp
    @property
    def base_hp(self):
        return self.__base_hp
    @abstractmethod
    def attack_enemy(self):
        pass
    def __add__(self, other):
        return self.__base_hp + other.base_hp
class MagicalStance:
    def attack_enemy(self):
        return 150.0
class Warrior(BaseCharacter):
    def __init__(self, hp, strength):
        super().__init__(hp)
        self.strength = strength
    def attack_enemy(self):
        return self.strength * 2.5
class Spellblade(Warrior, MagicalStance):
    def __init__(self, hp, strength):
        super().__init__(hp, strength)
    def attack_enemy(self):
        warrior_damage = Warrior.attack_enemy(self)
        magic_damage = MagicalStance.attack_enemy(self)
        return warrior_damage + magic_damage
class VolcanoZone:
    def activate_buff(self, character):
        print(
            "\n[Duck Typing]: Xác thực môi trường trận đấu thành công!"
        )
        print(
            "[Volcano Zone Effect]: "
            "Sức nóng dung nham kích hoạt!"
        )
        print(
            "Gia tăng +20% sát thương cho Warrior!"
        )
def apply_battleground_effect(environment, character):
    environment.activate_buff(character)
current_hero = None
def create_hero():
    global current_hero
    try:
        print("\n--- KHỞI TẠO MA KIẾM SĨ SPELLBLADE ---")
        hp = int(
            input("Nhập lượng máu cơ bản (HP): ")
        )
        strength = float(
            input("Nhập chỉ số sức mạnh (Strength): ")
        )
        current_hero = Spellblade(
            hp,
            strength
        )
        print(
            "\n[Thành công]: Khởi tạo nhân vật Spellblade thành công!"
        )
        mro_list = []
        for cls in Spellblade.__mro__:
            if cls.__name__ != "ABC":
                mro_list.append(
                    cls.__name__
                )
        print(
            "[MRO Architecture]:",
            " -> ".join(mro_list)
        )
        print(
            f"[Overloading __add__]: "
            f"Tổng HP tích lũy khi gộp đội hình: "
            f"{current_hero + current_hero}"
        )
    except ValueError:
        print(
            "Dữ liệu không hợp lệ!"
        )
def battle():
    global current_hero
    if current_hero is None:
        print(
            "Vui lòng khởi tạo nhân vật trước!"
        )
        return
    damage = current_hero.attack_enemy()
    print(
        f"\n[Đa hình] Spellblade vung kiếm ma thuật "
        f"gây tổng sát thương: {damage} DMG"
    )
    volcano = VolcanoZone()
    apply_battleground_effect(
        volcano,
        current_hero
    )
def show_menu():
    print("\n===== RPG GAME CORE MENU =====")
    print("1. Khởi tạo Ma kiếm sĩ Spellblade & Xem cấu trúc MRO")
    print("2. Ra lệnh tấn công & kích hoạt chiến trường (Duck Typing)")
    print("3. Thoát")

def main():
    while True:
        show_menu()
        choice = input("Chọn chức năng (0-2): ")
        match choice:
            case "1":
                create_hero()
            case "2":
                battle()
            case "3":
                print("Thoát chương trình!")
                break
            case _:
                print("Lựa chọn không hợp lệ!")
                
main()

