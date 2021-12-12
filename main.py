import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Window

import layout as l

def main():
    p = 0
    sg.theme('DarkPurple2')
    
    # all the stuff inside the window
    layout = [  
        [ sg.Text('Yatzee!')],
                [ sg.Text(''), sg.InputText()],
                [ sg.Button('OK'), sg.Button('Cancel')] ]

    # create the window
    Window = sg.Window('Yatzee!', layout)

    #event loot to process "events" and get the values of the inputs
    while True:

        event, values = Window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        print('You entered :', values[0])

        l.menu(p)
main()