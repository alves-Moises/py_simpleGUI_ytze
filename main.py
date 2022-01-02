from ctypes import alignment
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Window

import layout as l
import functions as f

import random as r

def main():
    p = 0
    sg.theme('DarkPurple2')
    name_list= list()
    
    # all the stuff inside the window
    i_dices = f.dices_ico()
    print(i_dices)
    
    layout = [  
        [ sg.Text('Yatzee!', justification='center')],
        [ sg.Image(i_dices[r.randint(1, 6)]), sg.Image(i_dices[r.randint(1, 6)]), sg.Image(i_dices[r.randint(1, 6)])],
        [ sg.HorizontalSeparator('#660099')],
        [ sg.Button('OK', pad=15)]
        ]

    # create the window
    Window = sg.Window('Yatzee!', layout)

    #event loot to process "events" and get the values of the inputs
    #getin players names
    while True:

        # first window
        event, values = Window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        if event == 'OK':
            Window.close()
        # print('You entered :', values[0])

        # get player name
        p = l.menu(p)
        names = l.players_name(p)
        for i in range(len(names)):
            name_list.append(names[i])

        #get initial scores
        score_list = f.get_score(name_list)
        
        print(score_list)

        
        
main()