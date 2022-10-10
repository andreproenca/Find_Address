import PySimpleGUI as sg


def findMyAddress(zipcode):
    import requests

    url = 'https://viacep.com.br/ws/%s/json/' % zipcode
    response = requests.get(url)
    response_json = response.json()
    return response_json


def screenApp():
    sg.theme("TanBlue")

    column1 = [
        [sg.Text('ZipCode: ', font='arial 10', pad=(0, 1))],
        [sg.Text('Address: ', font='arial 10', pad=(0, 1))],
        [sg.Text('District: ', font='arial 10', pad=(0, 1))],
        [sg.Text('City: ', font='arial 10', pad=(0, 1))],
        [sg.Text('State: ', font='arial 10', pad=(0, 1))],
        [sg.Text('DDD: ', font='arial 10', pad=(0, 1))],
    ]

    column2 = [
        [sg.Input(font='arial 10', pad=(0, 1), key='zipcode', size=(10, 0)),
         sg.Button('FindAddress', font='arial 7', size=(10, 0), pad=(2, 1))],
        [sg.Input(font='arial 10', pad=(0, 1), key='address')],
        [sg.Input(font='arial 10', pad=(0, 1), key='district')],
        [sg.Input(font='arial 10', pad=(0, 1), key='city')],
        [sg.Input(font='arial 10', pad=(0, 1), key='state', size=(4, 0))],
        [sg.Input(font='arial 10', pad=(0, 1), key='ddd', size=(4, 0))],
    ]

    layout = [
        [sg.Text('Find Brazilian Address ', font='arial 14 bold', pad=(0, 1), justification='center')],
        [sg.Column(column1, pad=((0, 20), 0)),
         sg.Column(column2)]

    ]

    mainScreen = sg.Window('Find Brazilian Address', element_padding=(0, 10), layout=layout, size=(400, 220),
                           finalize=True)
