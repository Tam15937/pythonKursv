import PySimpleGUI as win

import WFont

win.theme('DarkAmber')
winfont = WFont.winfont


def wirteData(val):
    f = open('resourses/usersLogin.txt', 'r', encoding="UTF-8")
    f.writelines(val[0])
    f.close()


def getData(security):
    f = open('resourses/usersData.txt', encoding="UTF-8")
    data = f.readlines()
    f.close()
    for i in data:
        if i.removesuffix('\n').split('+')[0] == security:
            return i.removesuffix('\n').split('+')[1]


def makeWindow(security: str):
    #  win.FileBrowse(file_types=(("Image Files", ("*.jpg", "*.png")),), key="-Img-")

    userData = getData(security).split(':')
    login = security.split(':')[0]
    password = security.split(':')[1]

    firstname = userData[0]
    name = userData[1]
    lastname = userData[2]
    phone = userData[3]
    address = userData[4]


    layout = [
        [
            win.Frame(title='Пользователь', layout=[
                [win.Text(text='Логин: ' + login, font=winfont)],
                [win.Text(text='Фамилия: ' + firstname, font=winfont)],
                [win.Text(text='Имя: ' + name, font=winfont)],
                [win.Text(text='Отчество: ' + lastname, font=winfont)],
                [win.Text(text='Номер телефона: ' + phone, font=winfont)]]
                      ),
            win.Image(filename='resourses/profileImage.png', key="profileImage", size=(300, 300))
        ]
    ]

    winUser = win.Window('Профиль', layout, resizable=True, element_justification='center', finalize=True)

    while True:
        event, values = winUser.read()
        if event == win.WIN_CLOSED or event == 'Cancel':
            break
    winUser.close()
