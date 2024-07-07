def password(n):
    result = ''
    for i in numbers:
        for j in numbers:
            if i >= j:
                continue
            elif n % (j + i) == 0:
                result = result + str(i) + str(j)
    return result
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
k = int(input('Введите число из первого поля: '))
print('Введите пароль: ', password(k))
