from RAG.rag.ingestion.loader import get_content
# Подключаем чтение исходного файла базы знаний.
from RAG.rag.ingestion.cleaner import clean_content
# Подключаем удаление учебного мусора и лишних пробелов.
from RAG.rag.ingestion.chunker import get_chunks
# Подключаем получение отдельных текстовых фрагментов.
from RAG.rag.ingestion.embedder import get_vectors
# Подключаем создание пары вектор и текст для каждого чанка.
from RAG.rag.ingestion.repository import save
# Подключаем сохранение подготовленных пар на диск.
def main():
# Объединяем подготовку индекса в один понятный сценарий.
 content = get_content()
 # Читаем строку из source/source.txt.
 cleaned = clean_content(content)
 # Получаем очищенную версию прочитанной строки.
 chunks = get_chunks(cleaned)
 # Получаем список фрагментов после очистки.
 if not chunks:
 # Проверяем, не исчез ли весь текст после подготовки.
  raise ValueError("Нет текста для индексирования")
 # Останавливаем запуск до перезаписи существующей базы.
 vectors = get_vectors(chunks)
 # Преобразуем каждый фрагмент в вектор и сохраняем связь с текстом.
 save(vectors)
 # Создаем или полностью обновляем database/database.txt.
 print("Сохранено фрагментов:", len(vectors))
 # Показываем количество записей, а не число координат.
if __name__ == "__main__":
# Проверяем, запущен ли модуль как программа, а не импортирован.
 main()
 # Выполняем индексирование только при явном запуске этого модуля.