import unittest
from main import *


class Testrep(unittest.TestCase):
    def test_rep(self):
        # Идёт проверка функции ответа бота, где мы подаём строку и ожидаем один из двух исходов
        # где для переменной game (нужна для отслеживания того, что продолжается диалог или нет)
        # и если True, то диалог продолжается, а если False, то диалог заканчивается, при этом в случае с True
        # требуется проверять, если есть слово, то ответить, если нет, то попросить научить
        self.assertEqual(reply('бра'), True)
        self.assertEqual(reply('пока'), False)

    def test_learn(self):
        # Идёт проверка функции учения бота, где мы подаём строку и бот запоминает наш ответ
        self.assertEqual(learn('мы боты'), True)
        self.assertEqual(learn('мы  не боты'), False)

    def test_isInUsRep(self):
        # Идёт проверка функции учения бота, где мы подаём строку и бот запоминает наш ответ
        main()
        self.assertEqual(isInUsRep('мы боты', 7), True)

if __name__ == '__main__':
    unittest.main()
