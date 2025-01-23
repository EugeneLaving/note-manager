username =input("Введите имя пользователя: ")
title1 =input("Введите первый заголовок: ")
title2 =input("Введите второй заголовок: ")
title3 =input("Введите третий заголовок: ")
content =input("Введите содержание заметки: ")
created_date =input("Дата создания (дд.мм.гг) ")
issue_date =input("Выполнить до (дд.мм.гг):  ")
note =[
    username,
    content,
    created_date,
    issue_date,
    [title1, title2, title3]
]
print(note, end=" ")
