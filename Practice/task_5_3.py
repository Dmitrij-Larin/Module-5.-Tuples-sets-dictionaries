products = {
    "HDD Toshiba": 2000,
    "SSD Samsung": 8000,
    "CPU AMD Rysen 7": 20000,
    "CPU AMD Rysen 5": 13000,
}

for key, value in products.items():
    products[key] = round(products[key] + (products[key] * 0.1))

print(products)
