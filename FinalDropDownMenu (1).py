import tkinter
import tkinter as ttk
from tkinter import *

locations = {'Home': [500, 50], 'Park': [150, 325], 'School': [550, 500], 'Hospital': [1000, 150]}
speed_mode = {'Walking': 5, 'Car': 40, 'Motor bike': 60}
signal = {'No traffic': 0, 'Light': 1, 'Medium': 2, 'Heavy': 3}
tt = {0: 'No traffic', 1:'Light', 2:'Medium', 3:'Heavy'}

start = ''
end=''
tmode=''
traffic_intensity=''

#returns user selections
def get_params():
    global x,y,tmode,traffic_intensity
    def get_data():
        global x,y,tmode,traffic_intensity
        x = clicked.get()
        y = clicked2.get()
        tmode = select_mode.get()
        traffic_intensity=clicked3.get()
        root.destroy()

    root = Tk()
    root.title('Simulator Options')
    # Adjust size
    root.geometry("400x400")

    # Dropdown menu options
    options = ['School', 'Hospital', 'Home', 'Park' ]

    #1st option: location
    # datatype of menu text
    clicked = StringVar()

    # initial menu text
    clicked.set("Enter Your current Location")

    # Create Dropdown menu
    drop = OptionMenu(root, clicked, *options)
    drop.pack()

    #second option: destination
    clicked2 = StringVar()

    clicked2.set("Enter your destination")

    drop2 = OptionMenu(root, clicked2, *options)
    drop2.pack()

    Modes=[
        ('Walking','Walking'),
        ('Car','Car'),
        ('Motor bike', 'Motor bike')
    ]

    select_mode=StringVar()
    select_mode.set(None)
    for text,mode in Modes:
        Radiobutton(root, text=text, variable=select_mode,value=mode).pack()

    options2 = [
        'No traffic',
        'Light',
        'Medium',
        'Heavy'
    ]

    clicked3 = StringVar()


    clicked3.set("Enter the intensity of traffic")

    # Create Dropdown menu
    drop = OptionMenu(root, clicked3, *options2)
    drop.pack()

    submit = Button(root, text="Submit", command=get_data).pack()
    submit = Button(root, text="Quit", command=root.destroy).pack()




    # Execute tkinter
    root.mainloop()
    return x,y,tmode,traffic_intensity
start,end,mode,traffic_intensity=get_params()


start=locations[x]
end=locations[y]
speed_mode=speed_mode[mode]
traffic_intensity=signal[traffic_intensity]



