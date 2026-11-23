from rag.ingestion.embedder import get_vector
from rag.ingestion.repository import get_similar_chunks
from llm.llm import get_ai_response

query = "Сколько дней занимает доставка?"

vector = get_vector(query)

chunks = get_similar_chunks(vector, top_k=2)

print(len(chunks))
for text, score in chunks:
    print(f"{text} — {score:.3f}")
print(get_ai_response(query, chunks, mode="demo"))

#
# строка кодирования - 7
# строка поиска -9
# строка выбора режима - 14