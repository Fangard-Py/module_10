import time
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())


if __name__ == "__main__":
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    line_time = time.time()
    print(f'Линейный вызов: {line_time:.6f} секунд')

    # Многопроцессный
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    multiprocessing_time = time.time() - start_time
    print(f"Многопроцессный вызов: {multiprocessing_time:.6f} секунд")
