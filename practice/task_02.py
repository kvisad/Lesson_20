from llm.promt_builder import build_prompt

query = "Где находится магазин?"
chunks = [("Адрес нашего магазина - город Берлин.", 0.85)]

promt = build_prompt(query, chunks)

print(promt)
print(query in promt)
print("Берлин" in promt)

# Исходный вопрос буз уточнений задает общую задачу, полный промт полноценно описывает
# какой именно результат и в каком виде мы хотим получить