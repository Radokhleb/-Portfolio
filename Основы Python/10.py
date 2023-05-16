number = int(input())
digit1 = number // 100
digit2 = number // 10 % 10
digit3 = number % 10
max_digit = max(digit1, digit2, digit3)
min_digit = min(digit1, digit2, digit3)

if digit1 <= digit2 <= digit3 or digit3 <= digit2 <= digit1:
    middle_digit = digit2
elif digit2 <= digit1 <= digit3 or digit3 <= digit1 <= digit2:
    middle_digit = digit1
else:
    middle_digit = digit3

if min_digit == 0 and middle_digit == 1:
    print(f"{middle_digit}{min_digit} {max_digit}{middle_digit}")
elif min_digit == 0 and middle_digit == 0:
    print(f"{min_digit}{max_digit} {max_digit}{middle_digit}")
elif min_digit == 0:
    print(f"{middle_digit}{min_digit} {max_digit}{middle_digit}")
else:
    print(f"{min_digit}{middle_digit} {max_digit}{middle_digit}")