a, b, c = map(int, input("Введите три стороны треугольника через пробел ").split())

if a + b > c and b + c > a and a + c > b:
    print("Это треугольник")
    if a != b and a != c and b != c:
        print("Этот треугольник разносторонний")

    elif a == b and b == c and c == a:
        print("Это треугольник равносторонний")

    elif a == b or b == c or c == a:
        print("Это треугольник равнобедренный")


else:
    print("Это не треугольник")
