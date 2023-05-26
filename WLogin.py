import PySimpleGUI as win
import resourses.Udata as udata
import WFont
import WUser

win.theme(WFont.theme)
winfont = WFont.winfont
import WRegistration


def checkLogin(security):
    headers: list = udata.getTable('login')[0]
    data: list = udata.getTable('login')[1]

    for i in data:
        login = str(i[headers.index('login')])
        password = str(i[headers.index('password')])
        if login == security[0] and password == security[1]:
            return True
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

            val = [str(values['логин']), str(values['пароль'])]
            if checkLogin(val):
                winLogin.close()
                WUser.makeWindow(val)
            else:
                win.popup_quick_message('Неверный логин или пароль.', font=winfont, background_color='White',text_color='Black')
        if event == 'Регистрация':
            winLogin.close()
            WRegistration.makeWindow()
    winLogin.close()
