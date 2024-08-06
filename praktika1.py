class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    """
    Класс пользователя, содержащий атрибуты: логин, пароль, возраст
    """

    def __init__(self, username   ):
        self.username = username
        self.password = password
        self.age = age


if __name__ == '__main__':
    database = Database()
    while True:
        choice = int(input('Приветствую! Выберите действие:\n1 - Вход\n2 - Регистрация\n'))
        if choice == 1:
            login = input('Введите логин: ')
            password = input('Введите пароль: ')
            if login in database.data:
                if password == database.data[login]:
                    print(f'Вход выполнен, приветствую {login}')
                    break
                else:
                    print('Неверный пароль\n')
            else:
                print(f'пользователя {login} не существует\n')
        if choice == 2:
            user = User(input('Введите логин:'), input('Введите пароль:'))
            database.add_user(user.username, user.password)
        print(database.data)