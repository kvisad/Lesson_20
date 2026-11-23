import json
# Подключаем преобразование JSON-текста в объекты Python.
from urllib.request import urlopen
# Подключаем функцию HTTP-запроса из стандартной библиотеки Python.
city = "Yerevan"
# Задаем город латиницей: Yerevan означает Ереван.
url = f"https://wttr.in/{city}?format=j1"
# Подставляем город в адрес; format=j1 запрашивает ответ в JSON.
with urlopen(url, timeout=20) as response:
# Выполняем GET-запрос; timeout ограничивает ожидание сетевой операции.
 status = response.status
 # Сохраняем HTTP-статус ответа; при успехе ожидаем 200.
 raw_text = response.read().decode("utf-8")
 # Читаем байты ответа и превращаем их в строку UTF-8.
data = json.loads(raw_text)
# Разбираем JSON-строку; верхний уровень ответа становится словарем.
current = data["current_condition"][0]
# Берем первый словарь из списка текущих погодных условий.
description = current["weatherDesc"][0]["value"]
# Из вложенного списка извлекаем текстовое описание погоды.
print("HTTP-статус:", status)
# Показываем код успешного HTTP-ответа.
print("Город:", city)
# Показываем город, который запросили у сервиса.
print("Температура:", current["temp_C"], "°C")
# Читаем температуру в градусах Цельсия по ключу temp_C.
print("Ощущается как:", current["FeelsLikeC"], "°C")
# Показываем ощущаемую температуру из отдельного поля ответа.
print("Влажность:", current["humidity"], "%")
# Выводим относительную влажность; API передает значение как строку.
print("Погода:", description)
# Выводим описание; по умолчанию оно приходит на английском языке.
