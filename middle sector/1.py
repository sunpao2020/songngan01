hour = int(input("ชั่วโมง: "))
minute = int(input("นาที: "))

if hour < 0 or minute < 0:
    print("โปรดใส่ข้อมูลที่ไม่ติดลบ")
else:
    total_hours = hour
    if minute > 0:
        total_hours += 1
    if total_hours <= 1:
        print("ค่าจอดรถ: 0 บาท")
    else:
        cost = (total_hours - 1) * 30
        print("ค่าจอดรถ:", cost, "บาท")
