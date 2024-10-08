def month_to_season(number):
    if  3 <= number <= 5:
        return "Весна"
    elif 6 <= number <= 8:
        return "Лето"
    elif 9 <= number <= 11:
        return "Осень"
    elif 12 and 1 and 2:
        return "Зима"
    else:
        return "Неверный номер месяца"
try:
    number = int(input("Введите номер месяца (1-12): "))
    print(month_to_season(number))
except ValueError:
    print("Пожалуста, введите целое число от 1 до 12.")