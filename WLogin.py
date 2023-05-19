import PySimpleGUI as win

win.theme('DarkAmber')
import WRegistration

def checkLogin(val):
    f = open('resourses/usersLogin.txt', 'r', encoding="UTF-8").readlines()
    if val + '\n' in f:
        return True
    else:
        return False


def makeLogin():
    layout = [
        [win.Text('Логин', font=36, expand_x=True, expand_y=True)],
        [win.InputText('', k='логин', font=36)],
        [win.Text('Пароль', font=36)],
        [win.InputText('', k='пароль', font=36)],
        [win.Button('Логин', font=36)],
        [win.Button('Регистрация', font=36)]
    ]
    winLogin = win.Window('Вход', layout, resizable=True, element_justification='center', finalize=True)

    while True:
        event, values = winLogin.read()
        if event == win.WIN_CLOSED or event == 'Cancel':
            break
        if event == 'Логин':
            val = str(values['логин']) + ':' + str(values['пароль'])
            if checkLogin(val):
                print('запускаем окно пользователя')
            else:
                print('выводим сообщение об ошибке логина или пароля')
        if event == 'Регистрация':
            winLogin.close()
            WRegistration.makeRegistratuon()
    winLogin.close()
