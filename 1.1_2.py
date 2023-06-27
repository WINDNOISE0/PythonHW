a = 9

for i in range(a+1):
    print()
    for j in range(a+1):

        c = i * j
        print("{:<9}".format(" " * 3 + str(i) + " * " + str(j) + " = " + str(c)), end="")
