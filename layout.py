from os import popen
from tkinter.constants import INSERT
from typing import Text
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Window, popup_error

def menu(p=0):

    # players numb
    layout = [ 
                [sg.Text('WELCOME TO MY WORLD!', expand_x=True)],
                [sg.Text('Number of players: ')],
                [sg.Input(expand_x=True), sg.Button('OK')]
            ]   
    Window = sg.Window('Yatzee', layout, size=(400, 500))
    
    #input
    event , values = Window.read()
    
    #input validaton
    valid = False
    while not valid:
        event , values = Window.read()
        valid = True
        if event == 'OK':
            try: 
                values[0] = int(values[0])                 
            except:
                valid = False
                sg.popup_error('Only numbers!')
                # event, values = Window.read()

            else: 
                if values[0] < 1:
                    valid = False
                    sg.popup('Invalid value!')   
                else:
                    Window.close()
      
    # Window.close()
    print('evento: ', event)
    return values[0]

def players_name(p):
    layout = [
                [sg.Text(f'Please the name of the {"player" if p == 1 else "players"}:')],
                [],
                [sg.Button('OK')]
            ]

    temp_l = list()        
    i = 0

    while i < int(p): 
        temp_l.append([[sg.Text(f'{[i+1]}: ')], [sg.Input()]])
        i += 1

    layout.insert(1, temp_l)
    
    Window = sg.Window('Players...', layout)

    valid, duplicate, void = False, False, False
    
    # validation of input names
    while not valid:
        event, names = Window.read()
        valid  = True
        
        for i in range(len(names)):
            #Verify if field are'nt empt
            if names[i] == '':
                popup_error(f'These fiels canot be empt!') 
                valid = False
                break

            #verify duplicated names                
            elif duplicate == False:
                for j in range(i+1, len(names)):
                    if names[i] == names[j]:
                        popup_error(f'Names cannot be duplicated!') 
                        valid = False
                        duplicate = True
                        break

        duplicate = False

    Window.close()
    return(names)