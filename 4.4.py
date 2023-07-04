def withdraw(num, index, sum_all, sum_limit, history_oper):
    sum_all, history_oper = over_limit(sum_all, sum_limit, history_oper)
    if sum_all >= num:
        if num % 50 == 0:
            if index % 3 == 0 and index != 0:
                comiss = on_three_comiss(num)
                comiss = limit(comiss)
            else:
                comiss = num / 100 * 1.5
                comiss = limit(comiss)

            sum_all -= (num + comiss)
            print("Выдача " + str(num) + " у.е, комиссия составила " + str(comiss))
        else:
            print("Сумма выдачи должна быть кратна 50 у.е")
    else:
        print("Не достаточно денежных средств")
    
    sum_all, history_oper = over_limit(sum_all, sum_limit, history_oper)
    index+= 1
    print("На вашем счете " + str(sum_all) + " у.е")
    return sum_all, index, history_oper

def reload(num, index, sum_all, sum_limit, history_oper):
    sum_all, history_oper = over_limit(sum_all, sum_limit, history_oper)
    if num % 50 == 0:
        sum_all += num
    else:
        print("Сумма пополнения должна быть кратна 50 у.е")

    
    sum_all, history_oper = over_limit(sum_all, sum_limit, history_oper)
    print("На вашем счете " + str(sum_all) + " у.е")
    index += 1
    return sum_all, index, history_oper

def on_three_comiss(num):
    comissa = num / 100 * 3
    return comissa

def limit(num):
    if num < 30:
        num = 30
    elif num > 600:
        num = 600

    return num

def over_limit(sum_all, sum_limit, history_oper):
    if sum_all > sum_limit:
        comissa = sum_all / 100 * 10
        sum_all -= comissa
        print("Сумма на вашем счету превышает 5000000, вычтен налог на богатство - " + str(comissa))
        history_oper.append(f'Вычтен налог на богатство {comissa:.2f}')
    return sum_all, history_oper



sum_all = 0
index = 1
sum_limit = 5000000
history_oper = []

while True:
    start = int(input("Здравствуйте, выберете операцию: 1 - внести ДС, 2 - снять ДС, 3 - посмотреть список операций, 4 - выйти "))
    if start == 4:
        break
    elif start == 1:
        val = int(input("Сколько вы хотите внести? (число должно быть кратно 50 у.е) "))
        sum_all, index, history_oper = reload(val, index, sum_all, sum_limit, history_oper)
        history_oper.append(f'Пополнение {val}')
    elif start == 2:
        sumw = int(input("Сколько вы хотите снять? (число должно быть кратно 50 у.е) "))
        sum_all, index, history_oper = withdraw(sumw, index, sum_all, sum_limit, history_oper)
        history_oper.append(f'Снятие {sumw}')
    elif start == 3:
        if len(history_oper) == 0:
            print("У вас не было операций")
        else:
            print(f'Ваши операции - {history_oper}')
    else:
        print("Вы ввели неверную операцию, повторите попытку")

