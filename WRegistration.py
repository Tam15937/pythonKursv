import PySimpleGUI as win

import WFont
import WLogin
import WUser

win.theme(WFont.theme)
winfont = WFont.winfont


def getData(security):
    f = open('resourses/usersData.txt', encoding="UTF-8")
    data = f.readlines()
    f.close()
    for i in data:
        if i.removesuffix('\n').split('+')[0] == security:
            return i.removesuffix('\n').split('+')[1]


def writeData(security, userData):
    f = open('resourses/usersData.txt', encoding="UTF-8")
    data = f.readlines()
    f.close()
    securityData = []
    usersData = []
    for i in data:
        i = i.removesuffix('\n').split('+')
        temp = i[0]
        securityData.append(temp)
        temp = i[1].split(':')
        usersData.append(temp)
    if security in securityData:
        win.popup_quick_message('Такой пользователь уже существует.', font=winfont)
        return False
    else:
        names = [i[1] for i in usersData]
        lastnames = [i[2] for i in usersData]
        tempUserData = userData.split(':')
        login = security.split(':')[0]
        password = security.split(':')[1]

        firstname = tempUserData[0]
        name = tempUserData[1]
        lastname = tempUserData[2]
        phone = tempUserData[3]
        address = tempUserData[4]
        if name not in names or lastname not in lastnames:
            f = open('resourses/usersData.txt', 'a+', encoding="UTF-8")
            f.write(security + '+' + userData + '\n')
            f.close()
            return True
        else:
            win.popup_quick_message('Такой пользователь уже существует.', font=winfont)


def makeWindow():
    winputinsize = 20
    wintextsize = 15
    layout = [
        [win.Text('Фамилия', font=winfont,size=wintextsize),
         win.InputText('', k='фам', font=winfont, size=winputinsize)],
        [win.Text('Имя', font=winfont,size=wintextsize),
         win.InputText('', k='имя', font=winfont, size=winputinsize)],
        [win.Text('Отчество', font=winfont,size=wintextsize),
         win.InputText('', k='отч', font=winfont, size=winputinsize)],
        [win.Text('Номер телефона', font=winfont,size=wintextsize),
         win.InputText('', k='тел', font=winfont, size=winputinsize)],
        [win.Text('Адрес', font=winfont,size=wintextsize),
         win.InputText('', k='адрес', font=winfont, size=winputinsize)],
        [win.Text('Пароль', font=winfont,size=wintextsize),
         win.InputText('', k='пароль', font=winfont, size=winputinsize)],

        [win.Button('Регистрация', font=winfont), win.Button('Назад', font=winfont)]
    ]
    winRegistr = win.Window('Регистрация', layout, resizable=True, element_justification='center', finalize=True)

    while True:
        event, values = winRegistr.read()
        if event == win.WIN_CLOSED or event == 'Cancel':
            break
        if event == 'Регистрация':
            security = (
                    str(values['имя'])[0].upper() +
                    str(values['фам'])[0].upper() +
                    str(values['фам'])[1::] + ':' +
                    str(values['пароль'])
            )
            userData = (
                    str(values['фам']) + ':' +
                    str(values['имя']) + ':' +
                    str(values['отч']) + ':' +
                    str(values['тел']) + ':' +
                    str(values['адрес'])
            )
            if writeData(security, userData):
                winRegistr.close()
                WUser.makeWindow(security)

        if event == 'Назад':
            winRegistr.close()
            WLogin.makeWindow()
    winRegistr.close()
