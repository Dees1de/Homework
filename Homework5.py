immutable_var = 6, True, 5.1 ,'текст'
print('Immutable tuple: ',immutable_var)
# immutable_var[0] = 300
# Элементы кортежа являются неизменяемыми значениями
mutable_list = [6, True, 5.1, 'текст']
mutable_list[0] = False
mutable_list[1] = 22
mutable_list[2] = 'Sasha'
mutable_list[3] = 0.2
print('Mutable list: ',mutable_list)
