products = {
    "HDD Toshiba": 2000,
    "SSD Samsung": 8000,
    "CPU AMD Rysen 7": 20000,
    "CPU AMD Rysen 5": 13000,
}

while True:
    product = input("Введите название товара: ")
    if product in products:
        print(f"Данный товар {product} уже есть в магазине и его цена {products[product]}")
        break
    elif product not in products:
        price = int(input("Введите стоимость товара: "))
        products[product] = price
        print(f"Товар {product} добавлен! Его цена: {price}")
        continue
    else:
        pass

print()
print(f"Товары в магазине: {products}")

