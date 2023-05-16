number = int(input())
string = ""
max_digit_in_string = 0
for i in range(number):
    digits = int(input())
    while digits > 0:
        integer = digits % 10
        if max_digit_in_string < integer:
            max_digit_in_string = integer
        else:
            pass
        digits //= 10
    string += str(max_digit_in_string)
    max_digit_in_string = 0
print(int(string))