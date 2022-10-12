# -*- coding: utf-8 -*-
from random import randint

robo_replics = []
user_replics = []
separator = ';'
RoboTalk = "Бот: "
robot_dk = "Я ещё не умею отвечать на ваш вопрос.\nЧто мне следует отвечать? (перечислите через ;)"
robot_thanks = "Спасибо! Теперь буду знать"
robot_excep_ans = "Хорошо, тогда продолжим общение"
robot_exception = "Вы написали сообщение без ошибки? (да/нет)"

def onStart() -> None:
    # Чтение из файла ответов
    with open('ans.txt', encoding='UTF-8') as ansfile:
        for st in ansfile:
            st = st.replace('\n', '')
            robo_replics.append(st.split(separator))

    # Чтение из файла реплик
    with open('rep.txt', encoding='UTF-8') as repfile:
        for st in repfile:
            st = st.replace('\n', '')
            user_replics.append(st)


# Функция записи в файлы
def exitProc(bot_reps, us_rep) -> None:
    end_char = '\n'
    with open('ans.txt', encoding='UTF-8', mode='a') as ansfile:
        ansfile.write(end_char + bot_reps)
    with open('rep.txt', encoding='UTF-8', mode='a') as repfile:
        repfile.write(end_char + us_rep)


# Функция обучения бота
def learn(us_rep: str) -> bool:
    print(RoboTalk + robot_exception)
    us_ans = input().lower()
    if us_ans == "да" or us_ans == "д":
        print(RoboTalk + robot_dk)
        # на случай, если разделитель по умолчанию для файлов
        # будет отличаться от разделителя для пользователя
        new_bot_rep = input()\
            .replace('; ', separator)\
            .replace(' ;', separator)\
            .replace(';', separator)
        exitProc(new_bot_rep, us_rep)
        user_replics.append(us_rep)
        robo_replics.append(new_bot_rep.split(separator))
        return True
    return False


# Функция получения рандомного ответа из массива ответов бота
def getRandomBotAnswer(answer_index: int) -> int:
    # если в массиве больше одного символа,
    # рекомендую сделать shuffle
    # и взять первое (нулевое) значение из массива
    return randint(0, len(robo_replics[answer_index]) - 1)


def isInUsRep(us_rep: str, us_rep_index: int) -> bool:
    if us_rep == user_replics[us_rep_index]:
        return True
    elif us_rep == user_replics[us_rep_index] + '?':
        return True
    elif us_rep == user_replics[us_rep_index]\
            [:len(user_replics[us_rep_index]) - 1]:
        return True
    return False


# Функция ответа бота при получении реплики от пользователя
def reply(us_rep='пока') -> bool:
    if us_rep == 'пока':
        # тут рандом будет
        print(RoboTalk + robo_replics[1][getRandomBotAnswer(1)])
        return False
    for i in range(len(user_replics)):
        if isInUsRep(us_rep, i):
            # тут рандом будет
            print(RoboTalk + robo_replics[i][getRandomBotAnswer(i)])
            return True
    if learn(us_rep):
        print(RoboTalk + robot_thanks)
    else:
        print(RoboTalk + robot_excep_ans)
    return True


# Основная функция, которая запускает цикл чат-бота и запрашивает реплики
def main():
    onStart()
    gameloop = True
    print('Для выхода напишите "пока"')
    while gameloop:
        print('Вы: ')
        rep = input().lower()
        gameloop = reply(rep)


if __name__ == '__main__':
    main()
