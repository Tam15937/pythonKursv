import PySimpleGUI as win

import WFont
import WUser

win.theme('DarkAmber')
winfont = WFont.winfont
import WRegistration


def checkLogin(val):
    f = open('resourses/usersData.txt', encoding="UTF-8")
    data = f.readlines()
    f.close()
    securityData = []
    for i in data:
        i = i.removesuffix('\n').split('+')
        securityData.append(i[0])

    if val in securityData:
        return True
    else:
        return False


def makeWindow():
    layout = [
        [win.Text('Логин', font=winfont, expand_x=True, expand_y=True)],
        [win.InputText('', k='логин', font=winfont)],
        [win.Text('Пароль', font=winfont)],
        [win.InputText('', k='пароль', font=winfont)],
        [win.Button('Логин', font=winfont)],
        [win.Button('Регистрация', font=winfont)]
    ]
    winLogin = win.Window('Вход', layout, resizable=True, element_justification='center', finalize=True)

    while True:
        event, values = winLogin.read()
        if event == win.WIN_CLOSED or event == 'Cancel':
            break
        if event == 'Логин':

            val = str(values['логин']) + ':' + str(values['пароль'])
            if checkLogin(val):
                winLogin.close()
                WUser.makeWindow(val)
            else:
                win.popup_quick_message('Неверный логин или пароль.', font=winfont, background_color='White',text_color='Black')
        if event == 'Регистрация':
            winLogin.close()
            WRegistration.makeWindow()
    winLogin.close()
