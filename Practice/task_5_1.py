products = {
    "HDD Toshiba": 2000,
    "SSD Samsung": 8000,
    "CPU AMD Rysen 7": 20000,
    "CPU AMD Rysen 5": 13000,
}

my_products = {}

total = 0

while len(my_products) < 3:
    product = input("Что вы хотите приобрести: ")
    if product not in products:
        print("Такого товара нет в наличии!")
        continue
    else:
        quantity = int(input("В каком количестве: "))
        if quantity > 0:
            my_products[product] = products[product] * quantity
            total += my_products[product]
        else:
            continue

print()
print("Вы приобрели:")

for key, value in my_products.items():
    print(f"{key}. {round(value / products[key])} штук. Стоимость {value}")

print(f"Общая стоимость: {total}")

