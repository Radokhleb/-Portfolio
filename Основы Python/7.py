low = 1
high = 1000
while low <= high:
    mid = (high + low) // 2
    print(mid)
    big_or_small = input()
    if big_or_small == "Угадал!":
        high = 0
    elif big_or_small == "Меньше":
        high = mid - 1
    elif big_or_small == "Больше":
        low = mid + 1
  