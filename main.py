#Функция ввода числа
def input_number():
    try:
        n = int(input("Введите число: "))
        return n
    except ValueError:
        print("Ошибка: введено не число!")


#Функция обратного отсчета
def counting_down(num):
    while num >= 0:
        print(num)
        num -= 1


#Основное тело функции
try:
    counting_down(input_number())
except TypeError:
    print("Программа завершена с ошибкой!")