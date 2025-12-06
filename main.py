print("Если расстояние - вводите в метрах, если время - то секунды")
print("Введите величины (через пробел):")
first = list(map(float, input().split()))
num_val = len(first)

sum_val = sum(first)
mid = sum_val / num_val

print(f"Среднее значение: {mid:.4f}")

listin = input("Введите \"список\", если хотите увидеть список доступных инструментов, и введите \"нет\", если не хотите: ")
listin = listin.lower()

if listin == "список":
    print("Список доступных инструментов: линейка(все виды), секундомер, гири")
else:
    pass

instrument = input("Введите инструмент: ").lower()
s_main = 0.0
s_main2 = 0.0
mass = 0.0

if instrument == "линейка":
    kind = int(input("Введите тип линейки (1 - ученическая, 2 - чертёжная, 3 - инструментальная, 4 - демонстрационная, 5 - измерительная): "))
    if kind == 1:
        s_main = 0.015
    elif kind == 2:
        s_main = 0.007
    elif kind == 3:
        s_main = 0.006
    elif kind == 4:
        s_main = 0.005
    elif kind == 5:
        s_main = 0.075

if instrument == "секундомер":
    s_main = 0.015

if instrument == "гири":
    mass = float(input("Введите массу тела в граммах(если число целое, например 15г, введите 15.0, с точкой и 0 в конце): "))
    print("Если предложенная гиря не использовалась, введите 0")
    hundred = int(input("Сколько 100 - граммовых гирь: "))
    fifty = int(input("Сколько 50 - граммовых гирь: "))
    twenty  = int(input("Сколько 20 - граммовых гирь: "))
    ten = int(input("Сколько 10 - граммовых гирь: "))
    five = int(input("Сколько 5 - граммовых гирь: "))
    two = int(input("Сколько 2 - граммовых гирь: "))
    one = int(input("Сколько 1 - граммовых гирь: "))
    zero_five = int(input("Сколько 500мг - граммовых гирь: "))
    zero_two_five = int(input("Сколько 250мг - граммовых гирь: "))
    zero_one = int(input("Сколько 100мг - граммовых гирь: "))
    s_main = (hundred*0.04+0.1 if hundred > 0 else hundred*0)+(fifty*0.03+0.1 if fifty > 0 else fifty*0)+(twenty*0.02+0.1 if twenty > 0 else twenty*0)+(ten*0.012+0.1 if ten > 0 else ten*0)+(five*0.008+0.1 if five > 0 else five*0)+(two*0.006+0.1 if two > 0 else two*0)+(one*0.004+0.1 if one > 0 else one*0)+(zero_five*0.02+0.1 if zero_five > 0 else zero_five*0)+(zero_two_five*0.02+0.1 if zero_two_five > 0 else zero_two_five*0)+(zero_one*0.02+0.1 if zero_one > 0 else zero_one*0)
sum_abs_diff = 0.0
if instrument != "гири":
    for i in first:
        abs_diff = abs(mid - i)
        sum_abs_diff += abs_diff

    random_error = sum_abs_diff / num_val

    absolute_error = random_error + s_main

    print(f"\nРезультаты:")
    print(f"Среднее значение: {mid:.4f}")
    print(f"Случайная погрешность: {random_error:.6f}")
    print(f"Приборная погрешность: {s_main:.4f}")
    print(f"Абсолютная погрешность: {absolute_error:.6f}")
    print(f"Относительная погрешность: {(absolute_error/mid*100):.4f}%")

    is_speed = int(input("\nХотите вычислить погрешность скорости? (1 - да, 0 - нет): "))

    if is_speed == 0:
        print("Программа завершает работу")
    else:
        print("\n=== Вычисление погрешности скорости ===")
    
        if instrument == "секундомер":
            print("Вы измеряли время, введите соответствующие расстояния (в метрах через пробел):")
            second_name = "расстояние"
        else:
            print("Вы измеряли расстояние, введите соответствующие времена (в секундах через пробел):")
            second_name = "время"
    
        second = list(map(float, input().split()))
    
        if len(second) != num_val:
            print(f"Ошибка: количество измерений должно совпадать ({num_val} измерений)")
        else:
            sum_second = sum(second)
            mid_second = sum_second / num_val
        
            if instrument == "секундомер":
                print("\nДля расстояния:")
                try:
                    kind = int(input("Введите тип линейки (1 - ученическая, 2 - чертёжная, 3 - инструментальная, 4 - демонстрационная, 5 - измерительная): "))
                    if kind == 1:
                        s_main2 = 0.015
                    elif kind == 2:
                        s_main2 = 0.007
                    elif kind == 3:
                        s_main2 = 0.006
                    elif kind == 4:
                        s_main2 = 0.005
                    elif kind == 5:
                        s_main2 = 0.075
                except ValueError:
                    print("Вы ввели неверное значение(вводите числа)")
        
            sum_abs_diff2 = 0.0
            for i in second:
                sum_abs_diff2 += abs(mid_second - i)
        
            random_error2 = sum_abs_diff2 / num_val
            absolute_error2 = random_error2 + s_main2
        
            print(f"\nПогрешность {second_name}:")
            print(f"Среднее значение: {mid_second:.4f}")
            print(f"Абсолютная погрешность: {absolute_error2:.6f}")

            if instrument == "секундомер":
                v_mid = mid_second / mid 
                rel_error_v = absolute_error2/mid_second + absolute_error/mid
                abs_error_v = v_mid * rel_error_v
            else:
                v_mid = mid / mid_second 
                rel_error_v = absolute_error/mid + absolute_error2/mid_second
                abs_error_v = v_mid * rel_error_v
        
            print(f"\nСредняя скорость: {v_mid:.4f} м/с")
            print(f"Абсолютная погрешность скорости: {abs_error_v:.6f} м/с")
            print(f"Относительная погрешность скорости: {(rel_error_v*100):.4f}%")
else:
    print(f"Абслютная погрешность массы: {s_main}")
    print(f"Относительная погрешность массы: {s_main/mass}%")