"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""
def check_strings(first: str, second:str):
  if not (isinstance(first, str)) or not(isinstance(second, str)):
    return 0
  elif first == second:
    return 1
  elif second == 'learn':
    return 3
  elif len(first) > len(second):
    return 2
  else:
    return -1

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    test_data = [
      (None, None, 0),#является ли то, что передано функции, строками 
      (None, "abc", 0), 
      ("abc", None, 0), 
      (1, 2, 0),
      ("abc", "abc", 1), #Если строки одинаковые, вернуть 1
      ("", "", 1),
      ("leadsfsdfdsf", "abcdef", 2),#Если строки разные и первая длиннее, вернуть 2
      ("LEARN", "", 2),
      ("LEARN", "learn", 3),#строки разные и вторая строка 'learn', возвращает 3
      ("qwerwqdqdwq", "learn", 3),
      ("abcd", "efgh", -1),#other -1
    ]
    
    for f_param, sec_param, expected in test_data:
      result = check_strings(f_param, sec_param)
      assert result == expected, f'first:{f_param}, second:{sec_param}, exp: {expected} result:{result}'
      print(result)
    
if __name__ == "__main__":
    main()
