# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.



from pathlib import Path
from random import randint, choices
from string import ascii_lowercase, digits

FORMAT = ["txt", "json", "py", "sql"]

def gen_ext(ext: str, name_len_min: int = 6, name_len_max: int = 30, min_bytes: int = 256, max_bytes: int = 4096, output_dir: str = ".") -> None:
    
        name = choices(f'{ascii_lowercase}{digits}_', k=randint(name_len_min, name_len_max))
        data = bytes(randint(0, 255) for _ in range(randint(min_bytes, max_bytes)))
        file_name = "".join(name)
        full_file_name = f'{file_name}.{ext}'
        file_path = Path(output_dir) / file_name

        if not file_path.parent.is_dir():
            file_path.parent.mkdir(parents=True, exist_ok=True)

        if not file_path.exists():
            with open(full_file_name, "wb") as file:
                file.write(data)
                print(f"Создан файл: {file_name}")
        else:
            print(f"Файл уже существует: {file_name}")



def gen_any_count(format_:list, count_files: int, output_dir: str=".") -> None:
    for _ in range(count_files):
        gen_ext(format_[randint(0,len(FORMAT)-1)], output_dir=output_dir)

if __name__ == "__main__":
    gen_any_count(FORMAT, randint(1,10), "./new_folder")