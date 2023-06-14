"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def random_predict_v2(predict_list, number: int = 1, left: int = 0,
                      right: int = 100, count: int = 0) -> int:
    if left <= right:
        mid = (right + left) // 2
        if predict_list[mid] == number:
            return count
        elif predict_list[mid] < number:
            return random_predict_v2(predict_list, number, mid + 1, right, 
                                     count + 1)
        else:
            return random_predict_v2(predict_list, number, left, mid - 1, 
                                     count + 1)
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
    # Инициализируем список для хранения счетчика попыток угадывания каждого числа
    count_ls = []
    # Фиксируем RANDOM SEED, чтобы эксперимент был воспроизводим
    np.random.seed(10)  
    # Инициализируем массив 1000 случайных чисел от 1 до 100 
    random_array = np.random.randint(1, 101, size=1000)
    # Инициализируем список последовательных чисел от 1 до 100, для угадывания случайных
    # чисел на основе бинарного поиска
    predict_list = list(range(1, 101))
    # Цикл последовательно считывает полученные числа из массива данных random_array
    for number in random_array:
        # Добавляем в список счетчиков, число количества попыток, который вернула  
        # применненая фун-я 
        count_ls.append(random_predict_v2(predict_list, number, count= 0))
    # Вычисляем среднее значение всех элементов списка count_ls и преобразуем в целое 
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game_v2(random_predict_v2)