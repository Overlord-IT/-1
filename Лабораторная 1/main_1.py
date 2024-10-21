numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
skip_fives1 = numbers[:4]
# Сумма
skip_fives = numbers[5:]
sum_of_numbers = sum(skip_fives1) + sum(skip_fives)
# Количество
count_of_numbers = len(numbers)
# Среднее арифметическое
average_of_numbers = (sum_of_numbers / count_of_numbers)
# Замена цифры
numbers[4] = average_of_numbers

print("Измененный список:", numbers)
