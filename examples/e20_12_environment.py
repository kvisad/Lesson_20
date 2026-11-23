import os
# Подключаем стандартный модуль Python; в нем уже есть функция getenv.
student = os.getenv("LAB_STUDENT", "не задано")
# Читаем LAB_STUDENT из окружения Python; при отсутствии получаем "не задано".
print("LAB_STUDENT:", student)
# Показываем учебное значение, полученное из настройки терминала.
