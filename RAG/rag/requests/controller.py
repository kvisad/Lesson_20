from rag.ingestion.embedder import get_vector
# Подключаем ту же модель векторов, что использовалась для базы.
from rag.ingestion.repository import get_similar_chunks
# Подключаем поиск наиболее похожих сохраненных фрагментов.
from llm.llm import get_ai_response
# Подключаем демонстрационный ответ или реальный вызов Gemini.
def get(request, top_k=2, mode="demo"):
# Описываем путь одного вопроса через поиск и получение ответа.
 request = request.strip()
 # Убираем случайные пробелы по краям вопроса.
 if not request:
 # Проверяем, есть ли в вопросе хотя бы один непробельный символ.
  raise ValueError("Введите непустой вопрос")
 # Не создаем вектор для пустого вопроса.
 vector = get_vector(request)
 # Превращаем вопрос в вектор той же моделью, что и чанки.
 chunks = get_similar_chunks(vector, top_k=top_k)
 # Находим до top_k фрагментов и их оценки сходства.

 return get_ai_response(request, chunks, mode=mode)
 # Передаем вопрос и найденные тексты выбранному обработчику.