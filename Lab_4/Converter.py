import csv
import json
from collections import OrderedDict

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r', newline='') as csvfile:       # TODO считать содержимое csv файла
        reader = csv.DictReader(csvfile)

        # Список для хранения словарей
        data = []

        # Проходим по каждой строке в CSV файле
        for row in reader:
            # Преобразуем каждую строку в словарь
            data.append(OrderedDict(row))

    # Преобразуем данные в JSON строку
    json_data = json.dumps(data, indent=4)        # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as f:
        f.write(json_data)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
