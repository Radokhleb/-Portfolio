number = int(input())
digit1 = number // 100
digit2 = number // 10 % 10
digit3 = number % 10
minimum = min(digit1, digit2, digit3)
maximum = max(digit1, digit2, digit3)
symms = minimum + maximum
if minimum < digit1 < maximum:
    midle = digit1
elif minimum < digit2 < maximum:
    midle = digit2
else:
    midle = digit3
pronzved = midle * 2
if symms == pronzved:
    print("YES")
else:
    print("NO")
