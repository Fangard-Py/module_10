from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power
        self.empty = 100
        self.day = 0

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.empty > 0:
            sleep(1)
            self.empty -= self.power
            self.day += 1
            if self.enemies < 0:
                self.enemies = 0

            print(f'{self.name} сражается {self.day}..., осталось {self.empty} воинов.')
        print(f'{self.name} одержал победу спустя {self.day} дней(дня)!')


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков и остановка текущего

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

# Вывод строки об окончании сражения
print('Все битвы закончились!')
