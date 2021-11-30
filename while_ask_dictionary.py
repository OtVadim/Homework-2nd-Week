# Цикл while: ask_user со словарём
# * Создайте словарь типа "вопрос": "ответ", например: 
#   {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
# * Напишите функцию ask_user_dict() которая с помощью input() просит 
#   пользователя ввести вопрос, а затем, если вопрос есть в словаре, 
#   программа давала ему соотвествующий ответ. Например:
#     Пользователь: Что делаешь?
#     Программа: Программирую

# Исключения: KeyboardInterrupt
# * Перепишите функцию ask_user() из задания while2, чтобы она 
#   перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
#   и завершала работу при помощи оператора break

answers = {"Как дела": "Хорошо!",
     "Что делаешь?": "Программирую", 
     "Получается?": "Иногда"}
     
question = input()

def talk_with(answers, question):
    try:
        while question != 0:
            print(answers.get(question))
            question = input()
    except KeyboardInterrupt:      #прикручена функция которая пишет "Пока", когда останавливаешь прогу
        return 'Пока!' 
            
print(talk_with(answers, question))




    