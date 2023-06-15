"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np
 
def random_predict_v2(predict_list, number: int = 1, left: int = 0,
                      right: int = 100, count: int = 0) -> int:
    
    """Угадавыем рандомные числа на основе алгоритма бинарного поиска 
       - применяем рекурсивный подход. Функция вызывает сама себя изменяя
       крайние значения массива с помощью которого мы угадываем число.

    Args:
        predict_list (_type_): список последовательных чисел от 1 до 100
        number (int, optional): Загаданное число. Defaults to 1.
        left (int, optional): Начальная позиция для поиска. Defaults to 0.
        right (int, optional): Конечная позиция для поиска. Defaults to 100.
        count (int, optional): Счетчик попыток. Defaults to 0.

    Returns:
        int: число попыток
    """
    
    # Ставим условие, что пока существует данный интервал цикл работает 
    if left <= right:
        # Вычисляем индекс середину массива данных predict_list
        mid = (right + left) // 2
        # Ставим условие, искомый элемент найден - возвращаем счетчик попыток
        if predict_list[mid] == number:
            return count
        # Искомый элемент больше нашей переменной 
        elif predict_list[mid] < number:
            # Функция вызывает саму себя, ищет число в правой стороне массива
            # добавляем попытку в счетчик
            return random_predict_v2(predict_list, number, mid + 1, right, 
                                     count + 1)
        else: # Искомый элемент меньше нашей переменной 
            # Функция вызывает саму себя, ищет число в левой стороне массива
            # добавляет попытку в счетчик
            return random_predict_v2(predict_list, number, left, mid - 1, 
                                     count + 1)
    # Если текущего элемента (number) не существует в нашем списке 
    # (predict_list), не для нашего случая
    else:
        return None

def score_game_v2(random_predict_v2) -> int:
    """Функция реализует подсчет среднего количества попыток поиска 
    случайнного числа из списка 1000 чисел. Здесь передаем "вычисляющую" 
    функцию random_predict_v2 в параметре.

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    # Инициализируем список для хранения счетчика попыток угадывания числа
    count_ls = []
    # Фиксируем RANDOM SEED, чтобы эксперимент был воспроизводим
    np.random.seed(10)  
    # Инициализируем массив 1000 случайных чисел от 1 до 100 
    random_array = np.random.randint(1, 101, size=1000)
    # Инициализируем список последовательных чисел от 1 до 100, для 
    # угадывания случайных чисел на основе бинарного поиска
    predict_list = list(range(1, 101))
    # Цикл последовательно считывает полученные числа из массива данных
    for number in random_array:
        # Добавляем в список счетчиков, число количества попыток, 
        # который вернула применненая фун-я 
        count_ls.append(random_predict_v2(predict_list, number))
    # Вычисляем среднее значение всех элементов списка count_ls и преобразуем 
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game_v2(random_predict_v2)