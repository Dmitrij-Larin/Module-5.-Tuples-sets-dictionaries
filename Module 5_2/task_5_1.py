words_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
}

words_medium = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать",
}

words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме",
}

levels = {0: "Нулевой",
          1: "Так себе",
          2: "Можно лучше",
          3: "Норм",
          4: "Хорошо",
          5: "Отлично",
          }

answers = {}

count = 0

while True:
    level = input("Выберите уровень сложности: лёгкий, средний или сложный: ").lower().strip()
    if level == "лёгкий":
        words = words_easy
        print("Вы выбрали лёгкий уровень сложности")
    elif level == "средний":
        words = words_medium
        print("Вы выбрали средний уровень сложности")
    elif level == "сложный":
        words = words_hard
        print("Вы выбрали сложный уровень сложности")
    else:
        words = words_easy
        print("Вам автоматически выбран лёгкий уровень сложности")

    for key, value in words.items():
        answer = input(f"{key}, {len(value)} букв, начинается на \"{value[0]}\"...").lower().strip()
        if answer == value:
            print(f"Верно! {key} - это {value}")
            answers.update({key: True})
            count += 1
        else:
            print(f"Неверно! {key} - это {value}")
            answers.update({key: False})
    break

print()
print(answers)
print()

keys_True = [key for key, value in answers.items() if value == True]
keys_False = [key for key, value in answers.items() if value == False]

print(f"Правильно отвеченны слова:\n"
    f"{'\n'.join(keys_True)}")
print()
print(f"Неправильно отвеченны слова:\n"
    f"{'\n'.join(keys_False)}")
print()
print(f"Ваш ранг:\n"
    f"{levels[count]}")
