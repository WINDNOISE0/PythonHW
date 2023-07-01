def find_items_backpack(items, max_weight):
    valid_combinations = []
    backpack_combination = []

    def backtrack(curr_weight, start_index):
        if curr_weight > max_weight:
            return

        if curr_weight == max_weight or start_index == len(items):
            valid_combinations.append(backpack_combination.copy())
            return

        for i in range(start_index, len(items)):
            item, weight = items[i]
            backpack_combination.append(item)
            backtrack(curr_weight + weight, i + 1)
            backpack_combination.pop()

    backtrack(0, 0)
    return valid_combinations


# Создаем словарь с вещами и их массой
items = {
    "Sleeping bag": 2,
    "Tent": 3,
    "Burner": 1,
    "Dishes": 2,
    "Food": 4
}

# Максимальная грузоподъемность рюкзака
max_backpack_weight = 7

# Поиск возможных вариантов комплектации рюкзака
combinations = find_items_backpack(list(items.items()), max_backpack_weight)

# Вывод результатов
if combinations:
    print("Possible options for backpack configuration:")
    for combination in combinations:
        print(combination)
else:
    print("There are no possible options for backpacking.")
    