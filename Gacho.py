"""Gà và Chó
Vừa gà vừa chó
Bó lại cho tròn
xxx con
yy chân chẵn
Hãy xác định số con gà và số con chó thỏa mãn yêu cầu.
Dữ liệu: Vào từ thiết bị nhập chuẩn gồm 1 dòng ghi 2 số nguyên xxx và yy (2≤ xxx, yy ≤ 10^9)
Kết quả: Đưa ra thiết bị xuất chuẩn một dòng 2 số nguyên số gà và số chó tìm được."""

a, b = map(int, input().split())
n = []
m = []
if b >= 2 or a <= (10**9):
    n = int((b-(2*a))/2)
    m = int(a - n)
    print(str(m) + " " + str(n))   
else:
    print("Loi!")
