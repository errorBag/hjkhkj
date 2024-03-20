numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

numbers_count = len(numbers)   # количество элементов в списке

numbers_one = numbers[:4]   # первая часть списка
numbers_two = numbers[5:]   # вторая часть списка
sum_numbers = sum(numbers_one + numbers_two)    # получаем сумму
average_of_numbers = float(sum_numbers / numbers_count)     # получаем среднее арифметическое
numbers_one += [average_of_numbers]     # прибавляем к первому списку среднее арифметическое
numbers = numbers_one + numbers_two     # создаём новый список

print("Измененный список:", numbers)