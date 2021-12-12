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
    while values[0]
    print(f'valor digitado: {values[0]}')