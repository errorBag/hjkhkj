# TODO Найдите количество книг, которое можно разместить на дискете
volume_disc = 1.44
volume_disc_kb = volume_disc * 1024
volume_disc_b = volume_disc_kb * 1024
str_book = 100
str_str = 50
symbol_in_str = 25
symbol_in_book = symbol_in_str * str_str * str_book
necessary_for_storage = symbol_in_book * 4
volume_book_in_disk = volume_disc_b / necessary_for_storage



print("Количество книг, помещающихся на дискету:", int(volume_book_in_disk))
