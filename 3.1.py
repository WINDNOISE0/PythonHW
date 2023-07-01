def countNum(string_text, dicter):
    for i in string_text:
        count = dicter.get(i, 0) + 1
        dicter[i] = count
    return dicter

dicter = {}
text_line = input("Input the text  ")


for i in text_line:
    dicter.update({i:text_line.count(i)})

result = countNum(text_line, dicter)
print(result)
print(dicter)

