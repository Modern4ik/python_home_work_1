# Программа для поиска суммы цифр трёхзначного числа.

user_number = 0
sum_digit = 0
flag = True

while flag:
    user_number = int(input("Введите трёхзначное число: "))
    
    if user_number > 99 and user_number < 1000:
        flag = False
    else:
        print("Ошибка ввода!Повторите попытку.")

while user_number / 10 > 0:
    sum_digit += user_number % 10

    user_number = user_number // 10

print("Сумма цифр в данном трёзначном числе равняется ->", sum_digit)