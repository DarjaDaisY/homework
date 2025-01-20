def print_params(a=1, b='строка', c=True):
    print(f"a = {a}, b = {b}, c = {c}")


print_params()
print_params(a=10)
print_params(a=10, b='другая строка')
print_params(c=[1, 2, 3])
print_params(b=25)
print_params(c=[1, 2, 3])


values_list = [42, "список", False]
values_dict = {'a': 3.14, 'b': "словарь", 'c': None}

print_params(*values_list)
print_params(**values_dict)


values_list_2 = [5, "два элемента"]
print_params(*values_list_2, 42)