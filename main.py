#Функция ввода числа
def input_number():
    global n
    try:
        n = int(input("Введите число: "))
    except ValueError:
        print("Ошибка: введено не число!")


#Функция обратного отсчета
def counting_down():
    global n
    while n >= 0:
        print(n)
        n -= 1


#Основное тело функции
input_number()
counting_down()