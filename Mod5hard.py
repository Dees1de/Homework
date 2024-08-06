import time
class User:

    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = int(hash(password))
        self.age = int(age)

    def __str__(self):
        return f'{self.nickname}'

class Video:

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = str(title)
        self.duration = int(duration)
        self.time_now = time_now
        self.adult_mode = adult_mode

class Urtube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        self.nickname = nickname
        password = hash(password)
        for i in ur.users:
            if i.nickname == self.nickname:
                if password == i.password:
                    self.current_user = i
                    break



    def register(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
        have = True
        for i in ur.users:
            if self.nickname in i.nickname:
                print(f'Пользователь {nickname} уже существует')
                have = False
        if have:
            self.users.append(User(nickname, password, age))
            ur.log_in(nickname, password)

    def log_out(self):
        ur.current_user = None

    def add(self, *args):
        list_ = list(args)
        for i in list_:
            self.videos.append(i)

    def get_videos(self, wf):
        finds =[]
        for i in ur.videos:
            if wf.lower() in i.title.lower():
                finds.append(i.title)
        return finds


    def watch_video(self, namevideo):
        if self.current_user == None:
            print("Войдите в аккаунт, чтобы смотреть видео")
        else:
            for i in ur.videos:
                if namevideo in i.title:
                    if i.adult_mode == True:
                        if ur.current_user.age < 18:
                            print("Вам нет 18 лет, пожалуйста покиньте страницу")
                        else:
                            for j in range(i.duration):
                                print(j + 1)
                                time.sleep(1)
                                if j == (i.duration - 1):
                                    print('Конец видео')
                    else:
                        for j in range(i.duration + 1):
                            print(j + 1)
                            time.sleep(1)
                            if j == (i.duration - 1):
                                print('Конец видео')

        pass


ur = Urtube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)

print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

print(ur.current_user)
ur.watch_video('Лучший язык программирования 2024 года!')



