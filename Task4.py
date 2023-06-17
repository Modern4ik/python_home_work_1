# Программа по поиску кол-ва сделанных журавликов каждым ребёнком, а именно: Петей, Серёжей и Катей.
# Известно, что Петя и Сережа сделали журавликов поровну, а Катя сделала в два раза больше, чем Петя и Серёжа вместе.

total_cranes = 0
flag = True

while flag:
    total_cranes = int(input("Введите общее кол-во журавликов, которое имеет чётное значение: "))

    if total_cranes >= 6 and total_cranes % 2 == 0:
        flag = False
    else:
        print("Ошибка ввода!Повторите попытку.")

petyas_cranes = (total_cranes // 3) // 2
sereja_cranes = petyas_cranes
katyas_cranes = (petyas_cranes + sereja_cranes) * 2

print(f"{total_cranes} - общее кол-во журавликов. Петя сделал журавликов в размере -> {petyas_cranes} , Катя в размере -> {katyas_cranes}, а Сережа в размере -> {sereja_cranes}")