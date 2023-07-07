a = ["Иван", "Андрей", "Николай"]
b = [1000, 1100, 1200]
c = [10.25]
dict_generator = {a[i]: b[i] + (b[i] / 100 * c[0]) for i in range(len(a))}

print(dict_generator)