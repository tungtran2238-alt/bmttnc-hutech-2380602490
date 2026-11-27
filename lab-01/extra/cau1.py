import itertools

danh_sach = [1, 2, 3]
hoan_vi = list(itertools.permutations(danh_sach))

print("Các hoán vị của danh sách", danh_sach, "là:")
for hv in hoan_vi:
    print(list(hv))