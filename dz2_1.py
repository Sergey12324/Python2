power_input = input("Введите степень: ").strip()
try:
    power = int(power_input)
except ValueError:
    print("Ошибка: степень должна быть целым числом.")
    exit()
elements = input("Введите числа через пробел: ").split()
result = []

for elem in elements:
    try:
        num = float(elem)
        if num.is_integer():
            num = int(num)
        powered = num ** power
        result.append(powered)
    except ValueError:
        if power < 0:
            result.append('')
        else:
            result.append(elem * power)

print("Вывод:", ' '.join(map(str, result)))