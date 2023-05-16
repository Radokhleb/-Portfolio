number = int(input())
new_list = []
for i in range(number):
    string = input()
    new_list.append(string)
for j in new_list:
    index = j.find("зайка")
    if index != -1:
        print(index + 1)
    else:
        print("Заек нет =(")