from RAG.rag.ingestion.embedder import get_vector
# Подключаем векторизацию вопроса той же моделью, что и база.
from RAG.rag.ingestion.repository import get_similar_chunks
# Подключаем чтение базы и сортировку по сходству.
query = "Можно ли оплатить заказ после получения?"
# Задаем вопрос об условиях оплаты.
vector = get_vector(query)
# Получаем один вектор с формой (384,).
chunks = get_similar_chunks(vector, top_k=2)
# Выбираем до двух результатов с максимальным сходством.
for text, score in chunks:
# Разбираем каждую найденную пару на текст и число.

 print(f"{score:.3f} | {text}")
 # Показываем оценку с тремя знаками и соответствующий фрагмент