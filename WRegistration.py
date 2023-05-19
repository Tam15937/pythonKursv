import PySimpleGUI as win

win.theme('DarkAmber')

layout = [
    [win.Text('Фамилия', font=36, expand_x=True, expand_y=True)],
    [win.InputText('', k='фам', font=36)],
    [win.Text('Имя', font=36)],
    [win.InputText('', k='имя', font=36)],
    [win.Text('Отчество', font=36)],
    [win.InputText('', k='отч', font=36)],
    [win.Text('Номер телефона', font=36)],
    [win.InputText('', k='тел', font=36)],
    [win.Text('Пароль', font=36)],
    [win.InputText('', k='пароль', font=36)],
    [win.Text('Логин', font=36)],
    [win.InputText('', k='логин', font=36)],
    [win.Button('Регистрация', font=36), win.Button('Назад', font=36)]
]
winRegistr = win.Window('Регистрация', layout, resizable=True, element_justification='center', finalize=True)


def wirteData(val):
    f = open('resourses/usersLogin.txt', 'r', encoding="UTF-8")
    f.writelines(val)
    f.close()


while True:
    event, values = winRegistr.read()
    if event == win.WIN_CLOSED or event == 'Cancel':
        break
    if event == 'Регистрация':
        val = [str(values['логин']) + ':' +
               str(values['пароль']) + ':' +
               str(values['фам']) + ':' +
               str(values['имя']) + ':' +
               str(values['отч']) + ':' +
               str(values['ном'])
               ]
        wirteData(val)
    if event == 'Назад':
        WLogin
winRegistr.close()
