# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

from pathlib import Path
import shutil

def sort_file(sourse_dir: str=".") -> None:
    sourse_dir_path = Path(sourse_dir)
    video_dir = sourse_dir_path / "Video"
    image_dir = sourse_dir_path / "Image"
    text_dir = sourse_dir_path / "Text"

    video_dir.mkdir(parents=True, exist_ok=True)
    image_dir.mkdir(parents=True, exist_ok=True)
    text_dir.mkdir(parents=True, exist_ok=True)

    for file_path in sourse_dir_path.iterdir():
        if file_path.is_file():
            extension = file_path.suffix[1:].lower()
            
            if extension in ["mp4", "avi", "mkv"]:
                shutil.move(file_path, video_dir / file_path.name)
            
            elif extension in ["jpg", "png", "gif"]:
                shutil.move(file_path, image_dir / file_path.name)
            
            elif extension in ["txt", "doc", "pdf"]:
                shutil.move(file_path, text_dir / file_path.name)

if __name__ == "__main__":
    sort_file()


