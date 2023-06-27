a = int(input("Введите число: "))
k = 0
while True:
    if a < 0 or a > 100000:
        break
    elif a == 1:
        print("Вы ввели единицу")
        break
    else:
        for i in range(2, a // 2+1):
            if (a % i == 0):
                k = k+1
        if (k <= 0):
            print("Число является простым")
            break
        else:
            print("Число является сложным")
            break

