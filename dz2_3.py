try:
    list1 = list(map(int, input("Введите первый список: ").split()))
except ValueError:
    print("Ошибка: первый список должен содержать только числа.")
    exit()

try:
    list2 = list(map(int, input("Введите второй список: ").split()))
except ValueError:
    print("Ошибка: второй список должен содержать только числа.")
    exit()

set1 = set(list1)
set2 = set(list2)
common_elements = sorted(set1 & set2)

print("Общие элементы:", ' '.join(map(str, common_elements)))