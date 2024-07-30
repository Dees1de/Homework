def calculate_structure_sum(list_):
    calc = 0
    for i in list_:
        if isinstance(i, int):
            calc += i
        if isinstance(i, str):
            calc += len(i)
        if isinstance(i, list):
            calc += calculate_structure_sum(i)
        if isinstance(i, set):
            list(i)
            calc += calculate_structure_sum(i)
        if isinstance(i, dict):
            keys = i.keys()
            list(keys)
            calc += calculate_structure_sum(keys)
            values = i.values()
            list(values)
            calc += calculate_structure_sum(values)
        if isinstance(i, tuple):
            list(i)
            calc += calculate_structure_sum(i)
    return calc

data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
result = calculate_structure_sum(data_structure)
print(result)
