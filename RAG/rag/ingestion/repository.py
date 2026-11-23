from pathlib import Path
# Подключаем пути к файлам проекта.
import numpy as np
# Подключаем создание числовых массивов из сохраненных координат.
from sklearn.metrics.pairwise import cosine_similarity
# Подключаем сравнение направлений двух векторов.
BASE = Path(__file__).resolve().parents[2]
# Находим корень Lesson_20 независимо от текущей папки терминала.
def get_database_path():
# Выделяем общий путь, который используют запись и чтение базы.
 return BASE / "database" / "database.txt"
 # Возвращаем путь; сам файл эта строка не создает.
def save(vectors):
# Принимаем пары вектор и текст для записи на диск.
 path = get_database_path()
 # Получаем путь к файлу индекса.
 path.parent.mkdir(parents=True, exist_ok=True)
 # Создаем папку database, если ее еще нет.
 with path.open("w", encoding="utf-8") as database:
 # Открываем файл для полной перезаписи текущей версии базы.
  for vector, text in vectors:
 # Получаем координаты и строку из каждой пары.
   vector_str = " ".join(map(str, vector))
 # Превращаем числа в строку с пробелами между ними.
   database.write(f"{vector_str};{text}\n")
 # Записываем координаты, разделитель, текст и перенос строки.

def get_similar_chunks(vector, top_k=2):
# Принимаем вектор вопроса и желаемое число результатов.
 if top_k <= 0:
 # Проверяем положительность числа результатов до чтения базы.
  raise ValueError("top_k должен быть больше 0")
 # Сообщаем, что ноль и отрицательные значения запрещены.
 chunks = []
 # Готовим список пар текст и оценка сходства.
 path = get_database_path()
 # Берем тот же путь, который использовала функция save.
 with path.open("r", encoding="utf-8") as database:
 # Читаем уже созданную базу; режим r ее не создает.
  for line in database:
 # Последовательно читаем записи, по одной строке на чанк.
   if not line.strip():
 # Проверяем, не является ли строка пустой или пробельной.
    continue
 # Пропускаем такую строку и переходим к следующей.
   raw_vector, text = line.rstrip("\n").split(";", 1)
 # Делим запись только по первой точке с запятой.
   numbers = [float(value) for value in raw_vector.split()]
 # Восстанавливаем числа из строк; плохое число вызовет ValueError.
   chunk_vector = np.array(numbers, dtype=float)
 # Получаем одномерный массив сохраненных координат.
   if chunk_vector.shape != vector.shape:
 # Проверяем одинаковое количество координат у вопроса и чанка.
    raise ValueError("Размерности векторов не совпадают")
 # Не сравниваем несовместимые массивы.
   score = cosine_similarity([vector], [chunk_vector])[0][0]
 # Из таблицы один на один извлекаем одну оценку сходства.
   chunks.append((text.strip(), float(score)))
 # Сохраняем исходный текст и его числовую оценку.
 if not chunks:
 # Проверяем, нашлась ли в файле хотя бы одна запись.
  raise ValueError("База пуста. Повторите индексирование")
 # Объясняем, что для поиска нужны сохраненные чанки.
 chunks.sort(key=lambda item: item[1], reverse=True)
 # Ставим записи с большей оценкой в начало списка.
 return chunks[:top_k]
 # Возвращаем не больше top_k записей в порядке убывания оценки.