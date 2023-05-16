love_manka = int(input())
live_ovsanca = int(input())
list_manka = []
list_ovsanka = []
for i in range(1, love_manka + live_ovsanca + 1):
    string_name = input()
    if i <= love_manka:
        list_manka.append(string_name)
    else:
        list_ovsanka.append(string_name)
set_all = set(list_manka) & set(list_ovsanka)
count = len(set_all)
if count > 0:
    print(count)
else:
    print("Таких нет")