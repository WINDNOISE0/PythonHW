ten_num = int(input("Введите ваше число в двоичной системе исчисления "))
tmp = ten_num
a,b,c,d,e = 11,12,13,14,15
arr = []

while ten_num > 0:
    if ten_num % 16 < 10:
        arr.insert(0, str(ten_num % 16))
    elif ten_num % 16 == 10:
        arr.insert(0, "a")
    elif ten_num % 16 == 11:
        arr.insert(0, "b")
    elif ten_num % 16 == 12:
        arr.insert(0, "c")
    elif ten_num % 16 == 13:
        arr.insert(0, "d")
    elif ten_num % 16 == 14:
        arr.insert(0, "e")
    elif ten_num % 16 == 15:
        arr.insert(0, "f")

    ten_num //= 16

arr = "".join(arr)

print(arr, hex(tmp), hex(tmp) == ("0x" + arr))


