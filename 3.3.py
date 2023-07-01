with open("3.2_article.txt", "r", encoding = "utf-8") as file:
    data = file.read()

text = data.split()

dirct = {}


for i in text:
    dirct.update({i:text.count(i)})

max_key = max(dirct, key=dirct.get)

print(max_key, dirct[max_key])
    

    



