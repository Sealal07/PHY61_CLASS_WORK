from sqlalchemy.sql.functions import next_value


def roman_to_decimal(roman_str):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    # MCMLXXXIV
    total = 0
    n = len(roman_str)
    for i in range(n-1):
        curr_value = roman_numerals[roman_str[i]]
        next_value = roman_numerals[roman_str[i+1]]
        if curr_value < next_value:
            total -= curr_value
        else:
            total += curr_value
    total += roman_numerals[roman_str[-1]]
    return str(total)

input1 = 'MCMLXXXIV'
input2 = 'MCCXXXIV'

print(f'Вход {input1} Выход: {roman_to_decimal(input1)}')
print(f'Вход {input2} Выход: {roman_to_decimal(input2)}')

print(roman_to_decimal('MMXXVI'))
print(roman_to_decimal('MMMLXXVIII'))
