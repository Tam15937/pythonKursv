import PySimpleGUI as win
import pandas as pd
import openpyxl as ox
import resourses.Udata
import numpy as np


def findUsernum(security):
    table = getTable('login')
    headers: list = table[0]
    userData: list = table[1]

    for i in userData:
        login = str(i[headers.index('login')])
        password = str(i[headers.index('password')])
        if login == security[0] and password == security[1]:
            return userData.index(i)


def getTable(sheet):
    path = 'resourses/Table.xlsx'
    excel_file_df = pd.read_excel(path, sheet_name=sheet)
    headers = excel_file_df.columns.to_numpy().tolist()
    data_array = excel_file_df.to_numpy().tolist()
    # ndarray
    return [headers, data_array]


def setTable(sheet, data: list, headers):
    path = 'resourses/Table.xlsx'
    data.insert(0, headers)
    with pd.ExcelWriter(path, mode='a', if_sheet_exists='replace') as writer:
        excel_file_df = pd.DataFrame(data=data)
        excel_file_df.to_excel(writer, sheet_name=sheet, index=False, header=False)
