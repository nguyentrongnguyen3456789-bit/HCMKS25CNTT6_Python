# Tính toán giá sản phẩm sau khi giảm giá
def calculate_payment(amount : float, rate: float) -> float:
    if amount < 0:
        print("Số tiền không được phép âm!")
        # raise ValueError("Số tiền âm!")
    # 100.0 - 10% -> 90.0
    if amount == 150.0:
        raise ValueError("Không được bằng 150!")
    return amount * (1 - rate)
calculate_payment(100.0, 0.1)

