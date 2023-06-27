import fractions

first_num, first_denum = map(int, input("Введите через пробел первые два числа - числитель и знаменатель ").split())
second_num, second_denum = map(int, input("Введите через пробел следующие два числа - числитель и знаменатель ").split())
first_val = fractions.Fraction(first_num, first_denum)
second_val = fractions.Fraction(second_num, second_denum)

do_it = input("Введите '+' если хотите сложить дроби или '*' если хотите их умножить ")
if do_it == "+":
    res = first_val + second_val
elif do_it == "*":
    res = first_val * second_val
else:
    print("Введено неверное значение")

print(res)