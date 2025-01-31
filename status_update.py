stat_dict = {"1": "Выполнено", "2": "В процессе", "3": "Отложено", "4": "Неизвестен"}
status = stat_dict.get("4")
print("Статус Вашей заметки: ", status.upper(), "\n Необходимо указать статус Вашей заметки! "
               "Возможные варианты:\n "
               "1. Выполнено\n 2. "
               "В процессе\n "
               "3. Отложено\n "
               "(Введите соответствующую цифру): ", end="")
status_inp = input()
while status_inp not in ["1","2","3"]:
    print("НЕКОРРЕКТНЫЙ ВВОД! Возможные варианты:\n "
            "1. Выполнено\n 2. "
            "В процессе\n "
            "3. Отложено\n",
            "(Введите соответствующую цифру): ", end="")
    status_inp = input()
else: # Иначе, выводим статус
    status = stat_dict.get(status_inp) # Эта строчка вытаскивает значения по ключу из словаря
    print("Статус Вашей заметки:", status.upper(), end="")