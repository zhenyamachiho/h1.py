a = True
while a:
    x = int(input("Введите трехзначное число: "))
    if 99 < x < 1000:
        a = False

print(f'Сумма цифр числа равна - {x // 100 + x // 10 % 10 + x % 10}')
