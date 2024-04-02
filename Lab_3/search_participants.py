participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

str_1 = participants_first_group.split('|')
str_2 = participants_first_group.split('|')
def find_common_participants(str_1, str_2, sep=','):
    str_1 = str_1.split(sep)
    str_2 = str_2.split(sep)
    result = []
    for i in str_1:
        if i in str_2:
            result.append(i)
    return sorted(result)
print(find_common_participants(participants_first_group, participants_second_group))
# TODO Провеьте работу функции с разделителем отличным от запятой