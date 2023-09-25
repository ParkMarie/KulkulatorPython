import math
k = True
while (k):
    print("Операции:")
    print("1. Сложение.")
    print("2. Вычитание.")
    print("3. Умножение.")
    print("4. Деление.")
    print("5. Возведение в степень.")
    print("6. Найти квадратный корень числа.")
    print("7. Найти факториал числа.")
    print("8. Найти синус числа.")
    print("9. Найти косинус числа.")
    print("10. Найти тангенс числа.")
    print("11. Выход.")
    while True:
        try:
            a = int(input("Введите операцию, которую хотели бы выполнить:"))
            break
        except ValueError:
            print("Ошибка! Введите именно число операции ;)")
    if a == 1:
        while True:
            try:
                num1 = int(input("Введите первое число:"))
                num2 = int(input("Введите второе число:"))
                print("Ответ:", num1 + num2)
                break
            except ValueError:
                print("Ошибочка вышла( Просим вас вводить только числа ;)")
    elif a == 2:
        while True:
            try:
                num1 = int(input("Введите первое число:"))
                num2 = int(input("Введите второе число:"))
                print("Ответ:", num1 - num2)
                break
            except ValueError:
                print("Ошибочка вышла( Просим вас вводить только числа ;)")
    elif a == 3:
        while True:
            try:
                num1 = int(input("Введите первое число:"))
                num2 = int(input("Введите второе число:"))
                print("Ответ:", num1 * num2)
                break
            except ValueError:
                print("Ошибочка вышла( Просим вас вводить только числа ;)")
    elif a == 4:
        while True:
            try:
                num1 = int(input("Введите первое число:"))
                num2 = int(input("Введите второе число:"))
                if num2 == 0:
                    print("На ноль делить нельзя ((")
                else:
                    print("Ответ:", num1 / num2)
                    break
            except ValueError:
                print("Ошибочка вышла( Просим вас вводить только числа ;)")
    elif a == 5:
        while True:
            try:
                num1 = int(input("Введите число:"))
                num2 = int(input("Введите степень числа:"))
                print("Ответ:", num1 ** num2)
                break
            except ValueError:
                print("Ошибочка вышла( Просим вас вводить только числа ;)")
    elif a == 6:
        while True:
            try:
                num1 = int(input("Введите число:"))
                print("Ответ:", num1 ** 0.5)
                break
            except ValueError:
                print("Ошибочка вышла( Просим вас вводить только числа ;)")
    elif a == 7:
        while True:
            try:
                num1 = int(input("Введите число:"))
                f = 1
                while num1 > 1:
                    f = f * num1
                    num1 = num1 - 1
                    print("Ответ:", f)
                    break
            except ValueError:
                print("Ошибка вышла( Просим вас вводить только числа ;)")
    elif a == 8:
        while True:
            try:
                num1 = int(input("Введите число:"))
                print("Ответ:", math.sin(num1))
                break
            except ValueError:
                print("Ошибочка вышла( Просим вас вводить только числа ;)")
    elif a == 9:
        while True:
            try:
                num1 = int(input("Введите число:"))
                print("Ответ:", math.cos(num1))
                break
            except ValueError:
                print("Ошибка вышла( Просим вас вводить только числа ;)")
    elif a == 10:
        while True:
            try:
                num1 = int(input("Введите число:"))
                print("Ответ:", math.tan(num1))
                break
            except ValueError:
                print("Ошибочка вышла( Просим вас вводить только числа ;)")
    elif a == 11:
        print("До новых встреч!")
        break
    else:
        print("Такой операции нет, выберите предложенные операции ;)")


