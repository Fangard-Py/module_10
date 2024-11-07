from queue import Queue
from threading import Thread
from time import sleep
import random


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        wait_time = random.randint(3, 10)
        sleep(wait_time)
        print(f'{self.name} покушал(а) и ушел(ла)\n')


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            free_table = next((table for table in self.tables if table.guest is None), None)
            if free_table:
                free_table.guest = guest
                guest.start()
                print(f'{guest.name} сел(а) за стол номер {free_table.number}\n')
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди\n')

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    # print(f'{table.guest.name} покушал(а) и ушел(ла)')
                    print(f'Стол номер {table.number} свободен\n')
                    table.guest = None

                if not self.queue.empty():
                    next_guest = self.queue.get()
                    table.guest = next_guest
                    next_guest.start()
                    print(f'{next_guest.name} вышел(ла) из очереди и сел(а) за стол номер {table.number}\n')
            sleep(0.1)


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Сириус Блек', 'Альбус Дамблдор', 'Римус Люпин', 'Полумна Лавгуд', 'Рон Уизли', 'Невилл Долгопупс',
    'Волан де Морт', 'Северус Снегг', 'Гермиона Грейнджер', 'Гарри Поттер', 'Минерва Макгонагалл', 'Альбус Дамблдор'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
