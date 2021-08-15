
import math
a = float(input())
b = float(input())
c = float(input())
if c<a+b and a<b+c and b<a+c:
    if a==b and b==c:
        s1 = round(float(0.25*math.sqrt((a+b+c)*a*b*c)), 2)
        print(f"Tam giac deu, dien tich = {s1}")
    elif a==b or b==c or a==c:
        s2 = round(float(0.25*math.sqrt((a+b+c)*(a+b-c)*(b+c-a)*(c+a-b))), 2)
        print(f"Tam giac can, dien tich = {s2}")
    elif a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b:
        s3 = round(float(0.25*math.sqrt((a+b+c)*(a+b-c)*(b+c-a)*(c+a-b))), 2)
        print(f"Tam giac vuong, dien tich = {s3}")
    else:
        s4 = round(float(0.25*math.sqrt((a+b+c)*(a+b-c)*(b+c-a)*(c+a-b))), 2)
        print(f"Tam giac thuong, dien tich = {s4}")
else:
    print("Khong phai tam giac")