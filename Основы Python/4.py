number_chaild = int(input())
name_max = ''
digit_max = 0

for i in range(number_chaild):
    name = input()
    digits = int(input())
    suma = 0  # обнуляем здесь, перед вычислением суммы цифр каждого имени
    while digits > 0:
        integer = digits % 10
        suma += integer
        digits //= 10
    if suma >= digit_max:
        digit_max = suma
        name_max = name

print(name_max)