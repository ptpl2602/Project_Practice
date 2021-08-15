import math
q = int(input())
lần_lặp = 0
while lần_lặp < q:
    n = int(input())
    danh_sách = list(map(int, input().split()))
    lần_lặp = lần_lặp + 1
    tong = sum(danh_sách)
    print(math.ceil(tong / n))
