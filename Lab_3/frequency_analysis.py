def count_letters(main_str):
    text = main_str.lower()
    letter_counts = {}
    for char in text:
        if char.isalpha() and char not in letter_counts:
            letter_counts[char] = 1
        elif char.isalpha():
            letter_counts[char] += 1
    return letter_counts


def calculate_frequency(letter_counts):
    count_of_letters = sum(letter_counts.values())
    frequency = {}
    for letter in letter_counts:
        frequency.update({letter: letter_counts[letter]/count_of_letters})
        sorted_keys = sorted(frequency.keys())
    return frequency


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

letter_counts_dict = count_letters(main_str)
frequency_collection = calculate_frequency(letter_counts_dict)
for item, value in frequency_collection.items():
    print(f'{item}: {value:.2f}')

