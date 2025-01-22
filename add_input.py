#Задание: grade 1 этап 1 задание 3
username =input("Введите своё имя: ")
title =input("Введите заголовок заметки: ")
content = input("Введите содержание заметки: ")
issue_date =input("Введите срок выполнения (дд.мм.гг): ")
created_date ="22.01.25"
print("Заметка создана:")
print("Имя пользователя: ", username)
print("Дата создания: ", created_date [0:5])
print("Выполнить до: ", issue_date [0:5])
print("Заголовок: ", title)
print("Содержание: ", content, end=" ")