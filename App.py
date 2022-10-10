from InterfaceAddress import *

screenApp()
while True:
    window, event, values = sg.read_all_windows()

    if event == sg.WIN_CLOSED:
        break

    try:
        street = findMyAddress(values['zipcode'])['logradouro']
        district = findMyAddress(values['zipcode'])['bairro']
        city = findMyAddress(values['zipcode'])['localidade']
        state = findMyAddress(values['zipcode'])['uf']
        ddd = findMyAddress(values['zipcode'])['ddd']

        window['address'].update(street)
        window['district'].update(district)
        window['city'].update(city)
        window['state'].update(state)
        window['ddd'].update(ddd)
    except:
        sg.Popup('Please, check the ZipCode number and your internet connection', font='arial 12', title='ERROR')
