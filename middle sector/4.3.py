min_val = None
while True:
    try:
        num = float(input("ใส่จำนวนจริงบวก: "))
        if num <= 0:
            break
        if min_val is None or num < min_val:
            min_val = num
    except:
        break

if min_val is not None:
    print("ค่าที่น้อยที่สุด:", min_val)
