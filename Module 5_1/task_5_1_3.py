my_things_set = {"Нож", "Топорик", "Складная пила", "Верёвка", "Удочка", "Компас", "Спички", "Палатка", "Аптечка", "Туристические ботинки"}
things_friend_set = {"Котелок", "Нож", "Брезент", "Спички", "Фильтр для воды", "Аптечка", "Надувная лодка", "Верёвка", "Спрей от насекомых", "Компас"}

# Вещи, которые бы взяли двое
set_my_and_friend = my_things_set.union(things_friend_set)
print(f"Вещи, которые бы взяли двое: {set_my_and_friend}")

# Вещи, которые бы взял только я
only_my_things_set = set_my_and_friend - things_friend_set
print(f"Вещи, которые бы взял только я: {only_my_things_set}")

# Вещи, которые бы взял только друг
only_things_friend_set = set_my_and_friend - my_things_set
print(f"Вещи, которые бы взял только друг: {only_things_friend_set}")

# Вещи, которые есть и у меня, и у друга
only_my_and_friend_set = my_things_set.intersection(things_friend_set)
print(f"Вещи, которые есть и у меня, и у друга: {only_my_and_friend_set}")