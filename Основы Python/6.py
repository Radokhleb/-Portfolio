number = int(input())
count = 0
i = 1
count2 = 0
string = ''
while True:
    start = i + 1
    count += 1
    if string != "":
        print(string)
        string = ""
        count2 = 0
    elif string == '' and i == number:
        break
    else:
        print(1)
        count += 1
    for i in range(start, number + 1):
        count2 += 1
        string += str(i) + " "
        if count == count2:
            break
        else:
            pass