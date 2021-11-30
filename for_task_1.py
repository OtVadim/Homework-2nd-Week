
#Цикл for: Оценки
#* Создать список из словарей с оценками учеников разных классов 
#  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
#* Посчитать и вывести средний балл по всей школе.
#* Посчитать и вывести средний балл по каждому классу.


class_scores = [
    {'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
    {'school_class': '4b', 'scores': [4, 2, 3, 5, 2]},
    {'school_class': '4a', 'scores': [3, 2, 2, 5, 2]}
]

def count_average(class_scores):
    scores_summ = 0                                   # ставим счетчик суммы на 0
    for score in class_scores:                        # перебираем переменные в class_score
        scores_summ += score                          # собираем сумму этих переменных
    scores_avg = scores_summ / len(class_scores)      # получаем  среднее из class_score
    return scores_avg

school_avg_summ = 0                                   # счетчик для подсчета общего успеха школы
for one_class in class_scores:                        # задаем перебираем словари в списке словарей
    class_avg = count_average(one_class['scores'])    # используем прошлую функцию к словаю с именем scores 
    print(f'средняя оценка для класса {one_class["school_class"]}:{class_avg}')
    school_avg_summ += class_avg                      # суммируем успеваемость классов

school_avg = round(school_avg_summ / len(class_scores), 2)  # округляем avg до двух знаков после запятой
print(f'Средняя оценка для школы: {school_avg}')



    
    