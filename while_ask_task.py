
# Цикл while: ask_user
# * Напишите функцию ask_user(), которая с помощью input() спрашивает 
#   пользователя “Как дела?”, пока он не ответит “Хорошо”


print('Как дела?')
answer = input()

def ask_user(answer):
    while answer != 'Хорошо':
        print('Как дела?')
        answer = input()
    if answer == 'Хорошо':
        return 'Правильно отвечаешь'

print(ask_user(answer))