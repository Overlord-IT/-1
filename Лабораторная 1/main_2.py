# TODO Найдите количество книг, которое можно разместить на дискете
pages = 100
lines = 50
symbols = 25
codes = 4
# Сколько байтов в 1 книге
bytes_in_symbols = codes * symbols
bytes_in_lines = lines * bytes_in_symbols
bytes_in_pages = pages * bytes_in_lines

# Перевести мегабайты в байты
mb = 1.44
kb = 1024
byte = 1024
sum_of_bytes = mb * kb * byte
# Находим количество книг
books = sum_of_bytes / bytes_in_pages
print("Количество книг, помещающихся на дискету:", round(books))
