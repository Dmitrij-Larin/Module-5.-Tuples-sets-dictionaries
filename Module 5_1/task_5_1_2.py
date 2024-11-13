cinema_genres = ("Комедия", "Экшн", "Пеплум", "Триллер")

# Заменим Экшн на Боевик
cinema_genres_list_1 = list(cinema_genres)
cinema_genres_list_1[1] = "Боевик"
new_cinema_genres = tuple(cinema_genres_list_1)
print(new_cinema_genres)
print()

# Добавим Фэнтези между Боевиком и Пеплумом
cinema_genres_list_2 = list(new_cinema_genres)
cinema_genres_list_2.insert(2, "Фэнтези")
new_cinema_genres_2 = tuple(cinema_genres_list_2)
print(new_cinema_genres_2)
print()

# Преобразуем кортеж в строку
str_cinema_genres = ', '.join(new_cinema_genres_2)
print(f"Обновлённые жанры кино: {str_cinema_genres}")