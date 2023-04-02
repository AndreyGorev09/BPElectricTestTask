import random


""" Дано положительное целочисленное 2-х байтное число. 
Нужно найти значение, которое будет, если поменять байты местами. """


def change_bytes(integer: int) -> int:
    print(f'Текущее число:{integer}') # выводим текущее число на печать

    check = 0 # счетчик
    last_list_bytes = [] # список для первого байта
    first_list_bytes = [] # список для второго байта
    bytes_str = bin(integer) # формирование числа в байты
    split_bytes_list = bytes_str.split('b') # получаем строку с байтами
    for i in split_bytes_list[1]:
        if check < 8: # перебираем первый байт
            last_list_bytes.append(i) # записываем значения в список
            
        elif check < 17: # перебираем второй байт
            first_list_bytes.append(i) # записываем значения в список
        check+=1 # для фильтрации увеличиваем счетчик на 1


    last_list_bytes, first_list_bytes = first_list_bytes, last_list_bytes # меняем байты местами

    new_list_bytes = last_list_bytes+first_list_bytes # создаем измененный список байт
    
    change_bytes_str = ''
    for i in new_list_bytes: # преобразуем список в строку
        change_bytes_str+=i 
    
    print(f'Число после перестановки байтов: {int(change_bytes_str, 2)}') # выводим новое число на печать

    

change_bytes(random.randint(0, 65535))
    
    