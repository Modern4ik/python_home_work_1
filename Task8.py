# Программа, которая получает от пользователя размеры плитки шоколада и проверяет, можно ли отломить количестово долек,
# заданное также пользователем, от данной плитки шоколада.

def get_value_from_user(message, error_message):
    flag = True

    while flag:
        user_value = int(input(message))

        if user_value > 0:
            return user_value
        else:
            print(error_message)


def check_choco_by_pieces(size_1, size_2, pieces):
    return pieces < size_1 * size_2 and (pieces % size_1 == 0 or pieces % size_2 == 0)
         

def print_report(res):
    if res:
        print("Да, мы можем отломить данное кол-во долек.")
    else:
        print("Нет. К сожалению мы не можем отломить данное кол-во долек.")


#####################################################################################################


choco_first_size = get_value_from_user("Введите первую размерность шоколадки: ", "Ошибка ввода.Повторите попытку!")
choco_second_size = get_value_from_user("Введите вторую размерность шоколадки: ", "Ошибка ввода.Повторите попытку!")
pieces_count = get_value_from_user("Введите желаемое кол-во долек: ", "Ошибка ввода.Повторите попытку!")

result = check_choco_by_pieces(choco_first_size, choco_second_size, pieces_count)

print()
print_report(result)