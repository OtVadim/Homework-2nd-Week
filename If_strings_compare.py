
# Условный оператор: Сравнение строк
# * Написать функцию, которая принимает на вход две строки
# * Проверить, является ли то, что передано функции, строками. 
#   Если нет - вернуть 0
# * Если строки одинаковые, вернуть 1
# * Если строки разные и первая длиннее, вернуть 2
# * Если строки разные и вторая строка 'learn', возвращает 3
# * Вызвать функцию несколько раз, передавая ей разные праметры 
#   и выводя на экран результаты

string1 = input()
string2 = input()

def compare(string1, string2):
    if string1.isdigit() == True and string2.isdigit() == True:
        return 0
    elif string1 == string2:
        return 1
    elif string1 != string2 and len(string1) > len(string2):
        return 2
    elif string1 != string2 and 'learn' in string2:
        return 3
    

print(compare(string1, string2))

string1 = input()
string2 = input()
print(compare(string1, string2))

string1 = input()
string2 = input()
print(compare(string1, string2))

string1 = input()
string2 = input()
print(compare(string1, string2))

