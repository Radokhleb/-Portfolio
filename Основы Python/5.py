number = int(input())
count_racer = 0
count_seconds = 0
first_start = 3
for i in range(0, number):
    count_seconds = first_start + i
    count_racer += 1
    while count_racer <= number:
        if count_seconds == 1:
            print(f"До старта {count_seconds} секунд(ы)")
            print(f"Старт {count_racer}!!!")
            break
        else:
            print(f"До старта {count_seconds} секунд(ы)")
            count_seconds -= 1