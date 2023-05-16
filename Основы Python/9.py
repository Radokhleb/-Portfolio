number1 = int(input())
number2 = int(input())
digit1 = number1 // 10
digit2 = number1 % 10
digit3 = number2 // 10
digit4 = number2 % 10
max_digit = max(digit1, digit2, digit3, digit4)
min_digit = min(digit1, digit2, digit3, digit4)
symma_center = (digit1 + digit2 + digit3 + digit4) - (max_digit + min_digit)
if len(str(symma_center)) == 2:
    symma_center = symma_center % 10
    print(f"{max_digit}{symma_center}{min_digit}")
else:
    print(f"{max_digit}{symma_center}{min_digit}")