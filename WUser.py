import PySimpleGUI as win
import pandas as pd
import numpy as np
import WFont

win.theme(WFont.theme)
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


def getTable():
    excel_file_df = pd.read_excel('resourses/Table.xlsx')
    headers = excel_file_df.columns.to_numpy().tolist()
    data_array = excel_file_df.to_numpy().tolist()
    # ndarray
    return win.Table(
        values=data_array,
        headings=headers,
        display_row_numbers=True,
        max_col_width=35,
        auto_size_columns=True,
        justification='right',
        num_rows=10,
        key='-TABLE-',
        row_height=35,
        tooltip="Grades Table"
    )


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

    tabProfile = win.Tab('Профиль', [
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
    ])

    tabGroup = win.Tab('Группа', [
        [
            win.Image(filename='resourses/profileImage.png', key="profileImage", size=(300, 300))
        ]
    ])

    tabTable = win.Tab('Рассписание', [
        [
            getTable()
        ]
    ])
    layout = [[
        win.TabGroup([[tabGroup, tabProfile,tabTable]])]
    ]

    winUser = win.Window('Профиль', layout=layout, resizable=True, element_justification='center', finalize=True)

    while True:
        event, values = winUser.read()
        if event == win.WIN_CLOSED or event == 'Cancel':
            break
    winUser.close()
