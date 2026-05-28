MAX_CHANCE = 5
SECRET_NUMBER = 27
flag = False

for i in range(1, MAX_CHANCE +1):
    your_choice = int(input(f"Lượt đoán {i} - Nhập số của bạn: "))
    if(your_choice == SECRET_NUMBER):
        print("=> Chúc mừng ! Bạn đã đoán chính xác mã số may mắn")
        break
    elif (your_choice >  SECRET_NUMBER):
        print("Gợi ý: Số của bạn lớn hơn số may mắn!")
    else:
        print("Gợi ý: Số của bạn nhỏ hơn số may mắn!")
# Cách 1
#     if(MAX_CHANCE == i): 
#         print("Bạn đã hết lượt đoán")
# Cách 2
# if(MAX_CHANCE == i and your_choice != SECRET_NUMBER): 
#     print("Bạn đã hết lượt đoán")
# Cách 3
    if(your_choice == SECRET_NUMBER):
        print("=> Chúc mừng ! Bạn đã đoán chính xác mã số may mắn")
        flag = True
        break
    else:
        if your_choice >  SECRET_NUMBER:
            print ("Lon hon so secret")
        else:
            print ("Nho hon so secret")

if not flag:
    print ("Het luot doan")