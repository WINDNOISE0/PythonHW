
def replacedName():
    for name in dir():
        if name.endswith('s') and name != 's':
            new_name = name[:-1]
            value = globals()[name]
            globals()[new_name] = value
            globals()[name] = None

sters = 1
prens = 2
foxes = 3
s = 'это не будет изменено'


print("До замены:", sters, prens, foxes, s)


before_replacement = [name for name in dir() if not name.startswith('__')]


replacedName()

print("После замены:", sters, prens, foxes, s)


after_replacement = [name for name in dir() if not name.startswith('__')]


if set(before_replacement) == set(after_replacement):
    print("Имена переменных не были изменены.")
else:
    print("Имена переменных были изменены.")