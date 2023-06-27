a = int(input("Введите количество рядов у ёлки? "))

b = "*"
d = " "

for i in range(a+1):
    print((d * a) + (b*i) + (d * a))
    a -= 1
