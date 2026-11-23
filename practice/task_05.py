from RAG.llm.promt_builder import build_prompt
from RAG.llm.llm import get_ai_response

query = "Сколько стоит доставка?"
chunks = [("Доставка занимает 3-5 дней", 0.9)]
promt = build_prompt(query, chunks)
print(promt)

# модель должна ответить, что в базе нет таких данных, т.к. мы это и написали в промте

print(get_ai_response(query, chunks, mode="gemini"))