MIN = 1
MAX = 999

while True:
    a = int(input("Введите ваше число "))
    if a < MIN or a > MAX:
        continue
    elif a / 10 < 1:
        b = a**2
        break
    elif a / 10 < 10 or a / 10 == 1:
        b = (a//10) * (a % 10)
        break
    elif a / 100 < 10 or a % 100 == 1:
        b = int(str(a % 10) + str(a // 10 % 10) + str(a // 100 % 10))
        break

print(b)



