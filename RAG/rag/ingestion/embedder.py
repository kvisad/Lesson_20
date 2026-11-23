from sentence_transformers import SentenceTransformer
# Подключаем класс моделей для получения векторов текста.
MODEL_NAME = "paraphrase-multilingual-MiniLM-L12-v2"
# Выбираем одну многоязычную модель для базы и всех вопросов.
model = SentenceTransformer(MODEL_NAME, device="cpu")
# Загружаем модель один раз при импорте модуля в этом процессе.
def get_vector(content):
# Принимаем одну строку, например вопрос пользователя.
 return model.encode(content, show_progress_bar=False)
 # Возвращаем один NumPy вектор из 384 чисел.
def get_vectors(chunks):
# Принимаем список текстовых фрагментов базы знаний.
 result = []
 # Готовим список связанных пар вектор и исходный текст.
 for chunk in chunks:
 # Перебираем фрагменты в исходном порядке.
  vector = get_vector(chunk)
 # Вычисляем вектор текущей строки уже загруженной моделью.
  result.append([vector, chunk])
 # Сохраняем вектор рядом с соответствующей строкой.
 return result
 # Возвращаем все пары после завершения цикла.
