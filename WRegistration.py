import PySimpleGUI as win
import resourses.Udata as udata
import WFont
import WLogin
import WUser

win.theme(WFont.theme)
winfont = WFont.winfont


def writeData(security, userData):
    headers: list = udata.getTable('login')[0]
    data: list = udata.getTable('login')[1]

    for i in data:
        login = str(i[headers.index('login')])
        password = str(i[headers.index('password')])
        firstname = str(i[headers.index('firstname')])
        name = str(i[headers.index('name')])
        lastname = str(i[headers.index('lastname')])
        if (login == security[0] and password == security[1]) or (name == userData[1] and lastname == userData[2]):
            win.popup_quick_message('Такой пользователь уже существует.', font=winfont)
            return False
    temp=security
    for i in userData:
        temp.append(i)
    data.append(security)
    udata.setTable('login', data, headers)
    return True


def makeWindow():
    winputinsize = 20
    wintextsize = 15
    layout = [
        [win.Text('Фамилия', font=winfont, size=wintextsize),
         win.InputText('', k='фам', font=winfont, size=winputinsize)],
        [win.Text('Имя', font=winfont, size=wintextsize),
         win.InputText('', k='имя', font=winfont, size=winputinsize)],
        [win.Text('Отчество', font=winfont, size=wintextsize),
         win.InputText('', k='отч', font=winfont, size=winputinsize)],
        [win.Text('Номер телефона', font=winfont, size=wintextsize),
         win.InputText('', k='тел', font=winfont, size=winputinsize)],
        [win.Text('Адрес', font=winfont, size=wintextsize),
         win.InputText('', k='адрес', font=winfont, size=winputinsize)],
        [win.Text('Пароль', font=winfont, size=wintextsize),
         win.InputText('', k='пароль', font=winfont, size=winputinsize)],

        [win.Button('Регистрация', font=winfont), win.Button('Назад', font=winfont)]
    ]
    winRegistr = win.Window('Регистрация', layout, resizable=True, element_justification='center', finalize=True)

    while True:
        event, values = winRegistr.read()
        if event == win.WIN_CLOSED or event == 'Cancel':
            break
        if event == 'Регистрация':
            security = [
                str(values['имя'])[0].upper() +
                str(values['фам'])[0].upper() +
                str(values['фам'])[1::],
                str(values['пароль'])
            ]
            userData = [
                str(values['фам']),
                str(values['имя']),
                str(values['отч']),
                str(values['тел']),
                str(values['адрес']),
                'schoolar'
            ]
            if writeData(security, userData):
                winRegistr.close()
                WUser.makeWindow(security)

        if event == 'Назад':
            winRegistr.close()
            WLogin.makeWindow()
    winRegistr.close()
