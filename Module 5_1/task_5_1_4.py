cinema_genres = ["комедия", "экшн", "пеплум", "триллер", "комедия", "пеплум"]

# Преобразуем список в множество
cinema_genres_set = set(cinema_genres)
print(cinema_genres_set)
print()

# Добавим 2 элемента в множество
cinema_genres_set.update(["хоррор", "фэнтези"])
print(cinema_genres_set)
print()

# Удалим элемент из множества
cinema_genres_set.remove("пеплум")
print(cinema_genres_set)
print()

# Удалим случайный элемент из множества
cinema_genres_set.pop()
print(cinema_genres_set)
print()

# Преобразуем множество обратно в список
new_cinema_genres = list(cinema_genres_set)
print(new_cinema_genres)



