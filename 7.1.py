# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.


from random import randint, choices
from string import ascii_lowercase, digits

FORMAT = ["txt", "json", "py", "sql"]

def gen_ext(ext: str, name_len_min: int = 6, name_len_max: int = 30, min_bytes: int = 256, max_bytes: int = 4096) -> None:
    
        name = choices(f'{ascii_lowercase}{digits}_', k=randint(name_len_min, name_len_max))
        data = bytes(randint(0, 255) for _ in range(randint(min_bytes, max_bytes)))
        with open(f'{"".join(name)}.{ext}', "wb") as file:
            file.write(data)


def gen_any_count(format_:list, count_files: int) -> None:
    for _ in range(count_files):
        gen_ext(format_[randint(0,len(FORMAT)-1)])

if __name__ == "__main__":
    gen_any_count(FORMAT, randint(1,10))