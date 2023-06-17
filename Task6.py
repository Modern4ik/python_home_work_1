# Программа для проверки автобусного билета на "счастливость".
# Т.е. сумма первым трёх цифр шестизначного числа и сумма последних трёх должна быть равна.

first_sum = 0
second_sum = 0

flag = True

while flag:
    
    user_number = int(input("Введите шестизначное число: "))

    if user_number > 99999 and user_number < 1000000:
        flag = False
    else:
        print("Ошибка ввода!Повторите попытку.")

while user_number / 10 > 0:

    if user_number > 999:
        second_sum += user_number % 10
    else:
        first_sum += user_number % 10
    
    user_number = user_number // 10

if first_sum == second_sum:
    print("Сумма первых трёх цифр билета с данным номером = {}, Сумма последних трёх цифр = {}. Данный билет является \"счастливым\". Поздравляю!:)".format(first_sum, second_sum))
else:
    print("Сумма первых трёх цифр билета с данным номером = {}, Сумма последних трёх цифр = {}. Данный билет не является \"счастливым\". Сожалею!:(".format(first_sum, second_sum))