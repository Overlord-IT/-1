# TODO Найдите количество книг, которое можно разместить на дискете
Pages = 100
Lines = 50
Symbols = 25
Codes = 4
# Сколько байтов в 1 книге
bytes_in_symbols = Codes * Symbols
bytes_in_lines = Lines * bytes_in_symbols
bytes_in_pages = Pages * bytes_in_lines

# Перевести мегабайты в байты
Mb = 1.44
Kb = 1024
Byte = 1024
sum_of_bytes = Mb * Kb * Byte
# Находим количество книг
books = sum_of_bytes / bytes_in_pages
print("Количество книг, помещающихся на дискету:", round(books))
