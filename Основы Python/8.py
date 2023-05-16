speed_pety = int(input())
speed_vasy = int(input())
speed_toly = int(input())
if speed_pety > speed_toly > speed_vasy:
    first = "Петя"
    second = "Толя"
    three = "Вася"
elif speed_pety > speed_vasy > speed_toly:
    first = "Петя"
    second = "Вася"
    three = "Толя"
elif speed_vasy > speed_toly > speed_pety:
    first = "Вася"
    second = "Толя"
    three = "Петя"
elif speed_vasy > speed_pety > speed_toly:
    first = "Вася"
    second = "Петя"
    three = "Толя"
elif speed_toly > speed_pety > speed_vasy:
    first = "Толя"
    second = "Петя"
    three = "Вася"
else:
    first = "Толя"
    second = "Вася"
    three = "Петя"
step1 = "   I   "
step2 = "   II   "
step3 = "   III   "
print(f"          {first}          ")
print(f"  {second}  ")
print(f"                  {three}  ")
print(f"{step2}{step1}{step3}")