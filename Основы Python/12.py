name_product = input()
price_product = int(input())
wiegth_product = int(input())
cash_in_user = int(input())
simvol = "=" * 16
simvol2 = "=" * 35
word = "Чек"
sdacha = cash_in_user - (wiegth_product * price_product)
itogo = wiegth_product * price_product
string_product = f"{name_product}"
string1 = f"{wiegth_product}кг * {price_product}руб/кг"
string2 = f"{cash_in_user}руб"
string3 = f"{sdacha}руб"
string4 = f"{itogo}руб"
print(f"{simvol}{word}{simvol}")
print(f"Товар: {string_product:>28}")
print(f"Цена: {string1:>29}")
print(f"Итого: {string4:>28}")
print(f"Внесено: {string2:>26}")
print(f"Сдача: {string3:>28}")
print(f"{simvol2}")