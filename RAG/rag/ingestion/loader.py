from pathlib import Path
# Подключаем создание путей, подходящих для macOS и Windows.
BASE = Path(__file__).resolve().parents[2]
# Поднимаемся от loader.py через ingestion и rag к папке Lesson_20.
def get_content():
# Описываем чтение исходной базы знаний из текстового файла.
 path = BASE / "source" / "source.txt"
 # Строим путь к файлу, который уже создали в папке source.
 return path.read_text(encoding="utf-8")
 # Читаем весь файл как строку; отсутствующий файл вызовет ошибку