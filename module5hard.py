class User:

    def __init__(self, username, password, age):
        self.username = str(username)
        self.password = int(hash(password))
        self.age = int(age)


class Video:

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = str(title)
        self.duration = int(duration)
        self.time_now = time_now
        self.adult_mode = adult_mode


class Urtube:

    def __init__(self, users, videos, current_user):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self):
        pass

    def register(self):
        pass

    def log_out(self):
        pass

    def add(self):
        pass

    def get_videos(self):
        pass

    def watch_video(self):
        pass
