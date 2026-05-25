print(' -- HỆ THỐNG TIẾP NHẬN BỆNH NHÂN ---');
name_patient = input('Nhập tên bệnh nhân:');
age = int(input('Mời bạn nhập tuổi:'));
symptom = input('Mời bạn nhập triệu chứng bệnh: ');

print(" -- PHIẾU KHÁM BỆNH --");
print(' Tên bệnh nhân', name_patient);
print(' Tuổi',age);
print(' Triệu chứng',symptom);

# vì sao không bị crash là do về cú pháp thì đúng hoàn toàn nhưng do
# gán sai biến nên khi in ra dữ liệu không khớp với dữ liệu đã nhập
# nguyên nhân gây lỗi logic là sai sót khi người làm nhầm lần giữa khác biến với nhau