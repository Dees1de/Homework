def print_params(a=1, b='String', c=True):
    print(a, b, c)


print_params()
print_params(True, 15, 'Alex')
print_params('Test', 35)
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = [False, 'Max', 4]
value_dict = {'a': True, 'b': 'Lexx', 'c': 44}

print_params(*values_list)
print_params(**value_dict)

values_list2 = ['Oleg', None]
print_params(*values_list2, 42)