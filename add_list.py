#Задание: grade 1 этап 1 задание 3
username =input("Введите своё имя: ")
title_1 =input("Введите первый заголовок: ")
title_2 =input("Введите второй заголовок: ")
title_3 =input("Введите третий заголовок: ")
titles =[title_1,  title_2, title_3]
content = input("Введите содержание заметки: ")
status = input("Введите статус заметки: ")
created_date =input("Введите дату начала (дд.мм.гг): ")
issue_date =input("Введите срок выполнения (дд.мм.гг): ")
print("Заметка создана:")
print("Имя пользователя: ", username)
print("Дата создания: ", created_date [0:5])
print("Выполнить до: ", issue_date [0:5])
print("Заголовки: ", titles)
print(title_1)
print(title_2)
print(title_3)
print("Содержание: ", content)
print("Статус: " status, end=" ")
