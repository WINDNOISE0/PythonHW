def withdraw(num):
    global i
    global sum
    over_limit(sum)
    if sum >= num:
        if num % 50 == 0:
            if i % 3 == 0 and i != 0:
                print
                comiss = on_three_comiss(num)
                comiss = limit(comiss)
            else:
                comiss = num / 100 * 1.5
                print(comiss)
                comiss = limit(comiss)

            sum -= (num + comiss)
            print("Выдача " + str(num) + " у.е, комиссия составила " + str(comiss))
        else:
            print("Сумма выдачи должна быть кратна 50 у.е")
    else:
        print("Не достаточно денежных средств")
    i+= 1
    print("На вашем счете " + str(sum) + " у.е")
    return sum, i

def reload(num):
    global i
    global sum
    over_limit(sum)
    if num % 50 == 0:
        sum += num
    else:
        print("Сумма пополнения должна быть кратна 50 у.е")

    print("На вашем счете " + str(sum) + " у.е")
    i += 1
    return sum, i

def on_three_comiss(num):
    comissa = num / 100 * 3
    return comissa

def limit(num):
    if num < 30:
        num = 30
    elif num > 600:
        num = 600

    return num

def over_limit(num):
    global sum_limit
    global sum
    if sum > sum_limit:
        comissa = num / 100 * 10
        sum -= comissa
        print("Сумма на вашем счету превышает 5000000, вычтен налог на богатство - " + str(comissa))
        return sum


sum = 0
i = 1
sum_limit = 5000000

while True:
    start = int(input("Здравствуйте, выберете операцию: 1 - внести ДС, 2 - снять ДС, 3 - выйти "))
    if start == 3:
        break
    elif start == 1:
        val = int(input("Сколько вы хотите внести? (число должно быть кратно 50 у.е) "))
        reload(val)
    elif start == 2:
        sumw = int(input("Сколько вы хотите снять? (число должно быть кратно 50 у.е) "))
        withdraw(sumw)
    else:
        print("Вы ввели неверную операцию, повторите попытку")

