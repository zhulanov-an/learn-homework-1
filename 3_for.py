"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    school_scores = [
        {'school_class': '4a', 'scores': [4, 4, 4, 5, 3]},
        {'school_class': '4b', 'scores': [4, 4, 4, 5, 3]},
        {'school_class': '5a', 'scores': [4, 4, 3, 5, 3]},
        {'school_class': '5b', 'scores': [4, 4, 3, 5, 3]},
        {'school_class': '7a', 'scores': [4, 4, 3, 5, 3]},
        {'school_class': '8a', 'scores': [4, 4, 5, 5, 3]},
        {'school_class': '9a', 'scores': [4, 4, 5, 4, 3]},
        {'school_class': '9b', 'scores': [4, 4, 4, 6, 3]},
        {'school_class': '10a', 'scores': [3, 4, 5, 5, 3]},
        {'school_class': '11a', 'scores': [3, 4, 4, 5, 3]},

    ]

    _sum_score_school = 0

    for class_ in school_scores:
        class_['avg_score'] = sum(class_['scores'])/len(class_['scores'])
        _sum_score_school += class_['avg_score']

    print(f'Средняя оценка по школе:{_sum_score_school/len(school_scores):.2f}')
    
    for class_ in school_scores:
      print(f'Средняя оценка по классу {class_["school_class"]}: {class_["avg_score"]:.2f}')

if __name__ == "__main__":
    main()
