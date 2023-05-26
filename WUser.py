import PySimpleGUI as win
import pandas as pd
import resourses.Udata as udata
import numpy as np
import WFont

win.theme(WFont.theme)
winfont = WFont.winfont


def makeTable(sheet):
    headers = udata.getTable(sheet)[0]
    data = udata.getTable(sheet)[1]

    return win.Table(
        values=data,
        headings=headers,
        display_row_numbers=True,
        max_col_width=35,
        auto_size_columns=True,
        justification='right',
        num_rows=10,
        key='-table-',
        row_height=35,
    )


def makeWindow(security):
    headers: list = udata.getTable('login')[0]
    userNum = udata.findUsernum(security)
    userData = udata.getTable('login')[1][userNum]
    login = str(userData[headers.index('login')])
    password = str(userData[headers.index('password')])

    firstname = str(userData[headers.index('firstname')])
    name = str(userData[headers.index('name')])
    lastname = str(userData[headers.index('lastname')])
    phone = str(userData[headers.index('phone')])
    adress = str(userData[headers.index('adress')])
    role = str(userData[headers.index('role')])

    tabProfile = win.Tab('Профиль', [
        [
            win.Frame(title='Пользователь', layout=[
                [win.Text(text='Логин: ' + login, font=winfont)],
                [win.Text(text='Фамилия: ' + firstname, font=winfont)],
                [win.Text(text='Имя: ' + name, font=winfont)],
                [win.Text(text='Отчество: ' + lastname, font=winfont)],
                [win.Text(text='Номер телефона: ' + phone, font=winfont)],
                [win.Text(text='Роль: ' + role, font=winfont)]]
                      ),
            win.Image(filename='resourses/profileImage.png', key="profileImage", size=(300, 300))
        ]
    ])

    tabGroup = win.Tab('Группа', [
        [
            win.Image(filename='resourses/profileImage.png', key="profileImage", size=(300, 300))
        ]
    ])

    tabTable = win.Tab('Рассписание', [
        [
            makeTable('table')
        ]
    ])
    layout = [[
        win.TabGroup([[tabProfile, tabGroup, tabTable]])]
    ]

    winUser = win.Window('Профиль', layout=layout, resizable=True, element_justification='center', finalize=True)

    while True:
        event, values = winUser.read()
        if event == win.WIN_CLOSED or event == 'Cancel':
            break
    winUser.close()
