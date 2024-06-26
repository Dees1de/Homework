my_dict = {'Alex': 1997, 'Leo': 2005, "Nik": 1930 }
print('Словарь',my_dict)
print('Существующее значение: ', my_dict['Alex'])
print('Не существующее значение: ', my_dict.get('lion'))
my_dict.update({'Gleb': 2002, 'Kate': 2004})
a = my_dict.pop('Leo')
print('Удаленное значение: ', a)
print('Измененный словарь:', my_dict)

my_set = {3,2,2,3,True, 3.2, "String", True, (2, 1)}
print('Множество: ', my_set)
my_set.add(52)
my_set.add('KEK')
my_set.remove(3)
print('Измененное ножество: ', my_set)