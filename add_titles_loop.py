print("Введите заголовки Ваших заметок. Когда напишите все - нажмите Enter")
titles=[]
title_input=input("Введите заголовок заметки: ")
while title_input != "":
    titles.append(title_input)
    title_input = input("Введите еще заголовок заметки: ")
    while title_input in titles:
        title_input = input("Данный заголовок уже есть! Введите другой, или нажмите Enter: ")
else:
    print(titles,  end=" ")