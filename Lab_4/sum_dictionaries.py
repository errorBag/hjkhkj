import json

def task(filename) -> float:
    # Открываем файл и читаем его содержимое
    with open(filename, 'r') as file:
        data = json.load(file)

    # Инициализируем переменную для хранения суммы произведений
    sum_of_products = 0.000

    # Перебираем все словари в данных
    for dictionary in data:
        # Получаем значения по ключам "score" и "weight"
        score = dictionary.get('score', '0')
        weight = dictionary.get('weight', '0')

        # Вычисляем произведение и добавляем к сумме
        sum_of_products += (score * weight)

    # Возвращаем сумму, округленную до трех знаков после запятой
    return round(sum_of_products, 3)

filename = 'input.json'
result = task(filename)
print(result)