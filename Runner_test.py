import logging
from runner_and_tournament import Runner
import unittest

logging.basicConfig(filename="runner_tests.log", level=logging.INFO, filemode='w', encoding="UTF-8",
                    format="s%(asctime)s| %(levelname)s| %(message)s-%(funcName)s")


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            r1 = Runner('Petr', -5)
            for _ in range(10):
                r1.walk()
            self.assertEqual(r1.distance, 50, f'{r1.name}Должен пробежать 50, а пробежал {r1.distance}')
            logging.info('"test_walk" выполнен успешно')
        except ValueError as exc:
            logging.warning("Неверная скорость для Runner", exc_info=exc)

    def test_run(self):
        try:
            r2 = Runner(2)
            for _ in range(10):
                r2.run()
            self.assertEqual(r2.distance, 100, f'{r2.name}Должен пробежать 100, а пробежал {r2.distance}')
            logging.info('"test_run" выполнен успешно')
        except TypeError as exc:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=exc)

    def test_challenge(self):
        r1 = Runner('Petr')
        r2 = Runner('iVAN')
        for _ in range(10):
            r1.walk()
            r2.run()
        self.assertNotEqual(r1.distance, r2.distance)


if __name__ == '__main__':
    unittest.main()