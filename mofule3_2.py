import re


def send_email(messege, recipient, sender='university.help@gmail.com'):
    if sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif (re.search('.com', sender) or re.search('.ru', sender) or re.search('.net', sender)) and re.search('@',sender):
        if (re.search('.com', recipient) or re.search('.ru', recipient) or re.search('.net', recipient)) and re.search('@', recipient):
            if sender == 'university.help@gmail.com':
                print('Письмо успешно отправлено с адреса ', sender, ' на адрес ', recipient)
            else:
                print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо успешно отправлено с адреса ', sender, ' на адрес ', recipient)
        else:
            print('Невозможно отправить письмо с адреса ', sender, ' на адрес ', recipient)
    else:
        print('Невозможно отправить письмо с адреса ', sender, ' на адрес ', recipient)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
