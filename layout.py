import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Window

def menu(p=0):
    # sg.themete('DarkAmber')
    layout = [ 
                [sg.Text('MENU')],
                [sg.Text('Number of players: ')],
                [sg.Input(default_text='1'), sg.Button('OK')],
                    ]   
    Window = sg.Window('Yatzee', layout)
    event , values = Window.read()
    while values[0]
    print(f'valor digitado: {values[0]}')