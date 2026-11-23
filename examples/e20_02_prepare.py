from ingestion.loader import get_content
# Подключаем чтение созданного нами source/source.txt.
from ingestion.cleaner import clean_content
# Подключаем очистку текста до разделения на фрагменты.
from ingestion.chunker import get_chunks
# Подключаем знакомое разбиение по точке и пробелу.
raw = get_content()
# Читаем грязный исходный текст из файла.
cleaned = clean_content(raw)
# Удаляем служебные символы и лишние пробелы.
chunks = get_chunks(cleaned)
# Получаем список текстовых фрагментов без векторов.
print(cleaned)
# Позволяем проверить текст после очистки.
print(len(chunks))
# Показываем количество подготовленных фрагментов.
print(chunks[0])
# Показываем первый фрагмент, который затем получит свой вектор