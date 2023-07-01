dictor = {
    "vlad":("socks", "knife", "water"),
    "dima":("light", "tent", "water"),
    "oleg":("light", "tent", "knife", "socks", "food")
}
common_items = []
a = []
for i in dictor:
    for j in dictor[i]:
        a.append(j)

print(a)
print(set(a))

for friend_items in dictor.values():
    if not common_items:
        common_items = list(friend_items)
    else:
        common_items = [item for item in common_items if item in friend_items]

for friend, items in dictor.items():
    if not any(item in common_items for item in items):
        print(f"Друг, у которого нет общих вещей: {friend}")
        break

