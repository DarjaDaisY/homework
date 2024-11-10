my_string = input('Введите что-то: ')
d = {'Спец.символы': 0, 'Буквы': 0, 'Цифры': 0}
for i in my_string:
    if i.isalpha():
        d['Буквы'] += 1
    elif i.isdigit():
        d['Цифры'] += 1
    else:
        d['Спец.символы'] += 1

print(d['Цифры']+d['Буквы']+d['Спец.символы'])
print(my_string.upper())
print(my_string.lower())
print(my_string.replace(' ',''))
print(my_string[0])
print(my_string[-1])