genres_of_literature = ("Роман", "Новелла", "Фэнтези", "Научная Фантастика")
nums = (3, 7, 9, 1, 6, 8, 2, 5, 4)

# Длина кортежа
print(f"Длина кортежа: {len(genres_of_literature)} элемента(-ов)")
print(f"Длина кортежа: {len(nums)} элемента(-ов)")
print()

# Максимальный и минимальный элементы кортежа
print(f"Максимальный элемент кортежа: {max(genres_of_literature)}\n"
      f"Минимальный элемент кортежа: {min(genres_of_literature)}")
print()
print(f"Максимальный элемент кортежа: {max(nums)}\n"
      f"Минимальный элемент кортежа: {min(nums)}")
print()

# Сумма элементов в кортеже
print(f"Сумма элементов в кортеже: {sum(nums)}")
print()

# Сортировка элементов кортежей в порядке возрастания
sorted_genres_of_literature = sorted(list(genres_of_literature))
sorted_nums = sorted(list(nums))

new_tuple_genres_of_literature = tuple(sorted_genres_of_literature)
new_tuple_nums = tuple(sorted_nums)

print(new_tuple_genres_of_literature)
print(new_tuple_nums)
print()

# Сортировка элементов кортежей в порядке убывания
genres_of_literature_list = list(genres_of_literature)
nums_list = list(nums)

genres_of_literature_list_reverse = sorted(genres_of_literature_list, reverse=True)
nums_list_reverse = sorted(nums_list, reverse=True)

tuple_genres_of_literature_reverse = tuple(genres_of_literature_list_reverse)
tuple_nums_reverse = tuple(nums_list_reverse)

print(tuple_genres_of_literature_reverse)
print(tuple_nums_reverse)













