from typing import Text
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Window

def menu(p=0):

    # players numb
    layout = [ 
                [sg.Text('MENU')],
                [sg.Text('Number of players: ')],
                [sg.Input(), sg.Button('OK')]
                    ]   
    Window = sg.Window('Yatzee', layout)
    
    #input
    event , values = Window.read()
    
    #input validaton
    if event == 'OK':
        try: 
            int(values[0])
        except:
            sg.popup_ok('Only numbers!')
            event, values = Window.read()

      
    Window.close()
    print('evento: ', event)
    return values[0]