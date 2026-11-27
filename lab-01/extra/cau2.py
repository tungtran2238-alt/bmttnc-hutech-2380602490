import re

chuoi = input("Nhập chuỗi: ")

cac_so = [int(so) for so in re.findall(r"-?\d+", chuoi)]

tong_duong = sum(abs(so) for so in cac_so)
tong_am = sum(so for so in cac_so if so < 0)

print(f"Giá trị dương: {tong_duong}. Giá trị âm: {tong_am}.")