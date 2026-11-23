import os
# Подключаем чтение режима из окружения.
from ingestion.embedder import get_vector
# Подключаем векторизацию вопроса.
from ingestion.repository import get_similar_chunks
# Подключаем поиск по готовому индексу.
from llm.prompt_builder import build_prompt
# Подключаем создание фактического промпта.
from llm.llm import get_ai_response
# Подключаем обработчик выбранного режима.
query = "Сколько стоит доставка?"
# Задаем вопрос, ответа на который нет в исходных фактах.
chunks = get_similar_chunks(get_vector(query), top_k=4)
# Берем все четыре факта, сохраняя порядок поиска.
print("Фактический промпт:")
# Печатаем подпись перед запросом.
print(build_prompt(query, chunks))
# Показываем правила, контекст и вопрос.
mode = os.getenv("RAG_MODE", "demo").strip().lower()
# Выбираем режим из текущего терминала.
print("Режим:", mode)
# Явно показываем, вызывается ли Gemini.
print("Ответ:")
# Печатаем подпись перед результатом.
print(get_ai_response(query, chunks, mode=mode))
# Получаем и выводим демонстрацию или реальный ответ.
