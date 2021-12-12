import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Window

import layout as l
import functions as f

def main():
    p = 0
    sg.theme('DarkPurple2')
    name_list= []
    
    # all the stuff inside the window
    layout = [  
        [ sg.Text('Yatzee!', justification='center')],
        [ sg.Text('')],
        [ sg.Button('OK', size=(300, 100))] 
        ]

    # create the window
    Window = sg.Window('Yatzee!', layout, size=(200, 100))

    #event loot to process "events" and get the values of the inputs
    while True:

        event, values = Window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        if event == 'OK':
            Window.close()
        # print('You entered :', values[0])

        p = l.menu(p)
        names = l.players_name(p)
        for i in range(len(names)):
            name_list.append(names[i])
        
        # print('P: ', p)
        # print('names: ', name_list)
        # print(names)
        
main()