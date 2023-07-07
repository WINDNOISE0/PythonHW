a = [1]
count = int(input("Ввведите количество чисел Фиббоначи "))
i = 0
while i < count-1:
    if a[i] == 1 and i < 1:
        a.append(1)
    else:
        a.append(a[i] + a[i-1])
    i+=1


print(a)


def gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = gen()

for i in range(count):
    print(next(fib_gen))