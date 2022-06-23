from tkinter import *
import random
import time
from tkinter import font
from tkinter.ttk import *
from turtle import window_height, window_width
from collections import deque
from FinalDropDownMenu import start, end, locations, speed_mode, traffic_intensity, mode, y
from PIL import ImageTk, Image

window = Tk()
window.title("Travel Time Simulator")
width = 1400
height = 650
speed = 180
Road_COLOR = 'white'

canvas = Canvas(window, bg='black', height=height, width=width)
canvas.pack()



class Road:
    def __init__(self):
        self.coordinates = []
        canvas.create_line(715, 50, 715, 65, fill='black', tag='Road', width=3)
        canvas.create_line(715, 50, 715, 65, fill='black', tag='Road', width=3)

        canvas.create_line(715, 225, 715, 240, fill='black', tag='Road', width=3)
        canvas.create_line(900, 100, 900, 115, fill='black', tag='Road', width=3)

        canvas.create_line(1000, 150, 1015, 150, fill='black', tag='Road', width=3)

        canvas.create_line(1000, 340, 1015, 340, fill='black', tag='Road', width=3)

        canvas.create_line(800, 500, 800, 515, fill='black', tag='Road', width=3)
        canvas.create_line(615, 550, 615, 565, fill='black', tag='Road', width=3)

        canvas.create_line(600, 325, 615, 325, fill='black', tag='Road', width=6)

        y = 600
        canvas.create_line(150, 600, 150, 0, fill='white', width=3)
        for i in range(y):
            self.coordinates.append([150, i + 1])
        x1 = 150
        x2 = 1000
        # canvas.create_line(x1, 550, x2, 550, fill='white', width = 3)
        canvas.create_line(165, 550, 250, 550, fill='white', width=3)
        canvas.create_line(265, 550, 600, 550, fill='white', width=3)
        canvas.create_line(615, 550, 1000, 550, fill='white', width=3)

        for i in range(x1, x2 + 1):
            self.coordinates.append([i, 550])
        y2 = 550
        y1 = 200
        # canvas.create_line(250, y1, 250, y2, fill='white', width = 3)
        canvas.create_line(250, 550, 250, 390, fill='white', width=3)
        canvas.create_line(250, 375, 250, 215, fill='white', width=3)
        canvas.create_line(250, 215, 165, 215, fill='white', width=3)

        for i in range(y1, y2 + 1):
            self.coordinates.append([250, i])

        x1 = 150
        x2 = 1000
        # canvas.create_line(x1, 50, x2, 50, fill='white', width = 3)
        canvas.create_line(165, 50, 500, 50, fill='white', width=3)
        canvas.create_line(515, 50, 700, 50, fill='white', width=3)
        canvas.create_line(715, 50, 1000, 50, fill='white', width=3)
        canvas.create_line(515, 65, 700, 65, fill='white', width=3)
        canvas.create_line(715, 65, 1000, 65, fill='white', width=3)

        for i in range(x1, x2 + 1):
            self.coordinates.append([i, 50])
        y1 = 25
        y2 = 225
        # canvas.create_line(500, y1, 500, y2, fill='white', width = 3)
        canvas.create_line(500, 25, 500, 50, fill='white', width=3)
        canvas.create_line(500, 65, 500, 200, fill='white', width=3)

        for i in range(y1, y2 + 1):
            self.coordinates.append([500, i])
        x1 = 515
        x2 = 1000
        # canvas.create_line(x1, 225, x2, 225, fill='white', width = 3)
        canvas.create_line(515, 225, 600, 225, fill='white', width=3)
        canvas.create_line(615, 225, 700, 225, fill='white', width=3)
        canvas.create_line(715, 225, 1000, 225, fill='white', width=3)

        for i in range(x1, x2 + 1):
            self.coordinates.append([i, 225])
        y1 = 25
        y2 = 225
        # canvas.create_line(700, y1, 700, y2, fill='white', width = 3)
        canvas.create_line(700, 25, 700, 50, fill='white', width=3)
        canvas.create_line(700, 65, 700, 100, fill='white', width=3)
        canvas.create_line(700, 115, 700, 225, fill='white', width=3)

        for i in range(y1, y2 + 1):
            self.coordinates.append([700, i])
        x1 = 150
        x2 = 400
        # canvas.create_line(x1, 375, x2, 375, fill='white', width = 3)
        canvas.create_line(165, 375, 250, 375, fill='white', width=3)
        canvas.create_line(265, 375, 400, 375, fill='white', width=3)

        for i in range(x1, x2 + 1):
            self.coordinates.append([i, 375])
        y2 = 500
        y1 = 325
        # canvas.create_line(400, y1, 400, y2, fill='white', width = 3)
        canvas.create_line(400, 325, 400, 375, fill='white', width=3)
        canvas.create_line(400, 390, 400, 500, fill='white', width=3)

        for i in range(y1, y2 + 1):
            self.coordinates.append([400, i])
        y2 = 550
        y1 = 100
        # canvas.create_line(600, y1, 600, y2, fill='white', width = 3)
        canvas.create_line(600, 100, 600, 225, fill='white', width=3)
        canvas.create_line(600, 240, 600, 325, fill='white', width=3)
        canvas.create_line(600, 340, 600, 500, fill='white', width=3)

        for i in range(y1, y2 + 1):
            self.coordinates.append([600, i])

        x1 = 600
        x2 = 1000
        # canvas.create_line(x1, 100, x2, 100, fill='white', width = 3)
        canvas.create_line(600, 100, 700, 100, fill='white', width=3)
        canvas.create_line(715, 100, 1000, 100, fill='white', width=3)

        for i in range(x1, x2 + 1):
            self.coordinates.append([i, 100])
        x1 = 250
        x2 = 500
        canvas.create_line(x1, 200, x2, 200, fill='white', width=3)
        for i in range(x1, x2 + 1):
            self.coordinates.append([i, 200])
        x1 = 400
        x2 = 1000
        canvas.create_line(x1, 325, x2, 325, fill='white', width=3)
        for i in range(x1, x2 + 1):
            self.coordinates.append([i, 325])
        x1 = 400
        x2 = 1000
        # canvas.create_line(x1, 500, x2, 500, fill='white', width = 3)
        canvas.create_line(415, 500, 600, 500, fill='white', width=3)
        canvas.create_line(615, 500, 1000, 500, fill='white', width=3)
        canvas.create_line(600, 550, 600, 515, fill='white', width=3)

        for i in range(x1, x2 + 1):
            self.coordinates.append([i, 500])
        y2 = 325
        y1 = 150
        # canvas.create_line(1000, y1, 1000, y2, fill='white', width = 3)
        # canvas.create_line(1000, y1, 1000, y2, fill='white', width = 3)

        for i in range(y1, y2 + 1):
            self.coordinates.append([1000, i])
        y2 = 325
        y1 = 25
        # canvas.create_line(1000, y1, 1000, y2, fill='white', width = 3)
        canvas.create_line(1000, 25, 1000, 50, fill='white', width=3)
        canvas.create_line(1000, 65, 1000, 225, fill='white', width=3)
        canvas.create_line(1000, 240, 1000, 325, fill='white', width=3)

        for i in range(y1, y2 + 1):
            self.coordinates.append([1000, i])

        x1 = 150
        x2 = 250
        # canvas.create_line(x1, 200, x2, 200, fill='white', width = 3)
        canvas.create_line(165, 200, 250, 200, fill='white', width=3)

        for i in range(x1, x2 + 1):
            self.coordinates.append([i, 200])

        y2 = 325
        y1 = 550
        # canvas.create_line(1000, y1, 1000, y2, fill='blue', width = 3)
        canvas.create_line(1000, 340, 1000, 500, fill='white', width=3)
        canvas.create_line(1000, 515, 1000, 550, fill='white', width=3)

        for i in range(y1, y2 + 1):
            self.coordinates.append([1000, i])

        canvas.create_line(1015, 550, 1015, 25, fill='white', width=3)
        canvas.create_line(1015, 25, 1000, 25, fill='white', width=3)
        canvas.create_line(615, 565, 1015, 565, fill='white', width=3)
        canvas.create_line(1015, 565, 1015, 550, fill='white', width=3)
        canvas.create_line(800, 515, 1000, 515, fill='white', width=3)
        canvas.create_line(715, 240, 1000, 240, fill='white', width=3)
        canvas.create_line(900, 115, 1000, 115, fill='white', width=3)

        canvas.create_line(1015, 150, 1015, 340, fill='white', tag='Road', width=3)
        canvas.create_line(165, 65, 500, 65, fill='white', tag='Road', width=3)
        canvas.create_line(615, 565, 615, 515, fill='white', tag='Road', width=3)
        canvas.create_line(615, 515, 800, 515, fill='white', tag='Road', width=3)
        canvas.create_line(800, 515, 800, 500, fill='white', tag='Road', width=3)
        canvas.create_line(615, 115, 615, 225, fill='white', tag='Road', width=3)
        canvas.create_line(615, 325, 615, 240, fill='white', tag='Road', width=3)
        canvas.create_line(615, 340, 615, 500, fill='white', tag='Road', width=3)
        canvas.create_line(615, 240, 715, 240, fill='white', tag='Road', width=3)
        canvas.create_line(715, 240, 715, 115, fill='white', tag='Road', width=3)
        canvas.create_line(715, 115, 900, 115, fill='white', tag='Road', width=3)
        canvas.create_line(900, 115, 900, 100, fill='white', tag='Road', width=3)
        canvas.create_line(1000, 150, 1015, 150, fill='white', tag='Road', width=3)
        canvas.create_line(265, 390, 265, 550, fill='white', tag='Road', width=3)
        canvas.create_line(415, 340, 415, 500, fill='white', tag='Road', width=3)
        canvas.create_line(400, 515, 600, 515, fill='white', tag='Road', width=3)
        canvas.create_line(515, 25, 515, 225, fill='white', tag='Road', width=3)
        canvas.create_line(500, 25, 515, 25, fill='white', tag='Road', width=3)
        canvas.create_line(265, 375, 265, 215, fill='white', tag='Road', width=3)
        canvas.create_line(265, 215, 500, 215, fill='white', tag='Road', width=3)
        canvas.create_line(500, 215, 500, 240, fill='white', tag='Road', width=3)
        canvas.create_line(500, 240, 600, 240, fill='white', tag='Road', width=3)
        canvas.create_line(615, 115, 700, 115, fill='white', tag='Road', width=3)
        canvas.create_line(715, 25, 715, 100, fill='white', tag='Road', width=3)
        canvas.create_line(715, 25, 700, 25, fill='white', tag='Road', width=3)
        canvas.create_line(400, 500, 400, 515, fill='white', tag='Road', width=3)
        canvas.create_line(165, 600, 165, 565, fill='white', tag='Road', width=3)
        canvas.create_line(165, 550, 165, 390, fill='white', tag='Road', width=3)
        canvas.create_line(165, 375, 165, 65, fill='white', tag='Road', width=3)
        canvas.create_line(165, 50, 165, 0, fill='white', tag='Road', width=3)
        canvas.create_line(165, 390, 250, 390, fill='white', tag='Road', width=3)
        canvas.create_line(265, 390, 400, 390, fill='white', tag='Road', width=3)
        canvas.create_line(165, 565, 615, 565, fill='white', tag='Road', width=3)
        canvas.create_line(415, 340, 600, 340, fill='white', tag='Road', width=3)
        canvas.create_line(615, 340, 1015, 340, fill='white', tag='Road', width=3)
        canvas.create_line(415, 340, 415, 390, fill='white', tag='Road', width=3)

        canvas.create_line(715, 50, 715, 65, fill='black', tag='Road', width=3)
        canvas.create_line(715, 50, 715, 65, fill='black', tag='Road', width=3)

        canvas.create_line(715, 225, 715, 240, fill='black', tag='Road', width=3)
        canvas.create_line(900, 100, 900, 115, fill='black', tag='Road', width=3)

        canvas.create_line(1000, 150, 1015, 150, fill='black', tag='Road', width=3)

        canvas.create_line(1000, 340, 1015, 340, fill='black', tag='Road', width=3)

        canvas.create_line(800, 500, 800, 515, fill='black', tag='Road', width=3)
        canvas.create_line(615, 550, 615, 565, fill='black', tag='Road', width=3)

        canvas.create_line(600, 325, 615, 325, fill='black', tag='Road', width=6)



def search(x, y):
    queue.append((x, y))
    solution[x, y] = x, y
    print(Road.coordinates)

    while queue:
        x, y = queue.popleft()
        if [x - 25, y] in Road.coordinates and (x - 25, y) not in visited:
            cell = (x - 25, y)
            solution[cell] = x, y
            queue.append(cell)
            visited.add((x - 25, y))

        if [x, y - 25] in Road.coordinates and (x, y - 25) not in visited:
            cell = (x, y - 25)
            solution[cell] = x, y
            queue.append(cell)
            visited.add((x, y - 25))
            print(solution)

        if [x + 25, y] in Road.coordinates and (x + 25, y) not in visited:
            cell = (x + 25, y)
            solution[cell] = x, y
            queue.append(cell)
            visited.add((x + 25, y))

        if [x, y + 25] in Road.coordinates and (x, y + 25) not in visited:
            cell = (x, y + 25)
            solution[cell] = x, y
            queue.append(cell)
            visited.add((x, y + 25))


def backRoute(x, y):
    path = []
    path.append((x, y))
    while (x, y) != (start_x, start_y):
        x, y = solution[x, y]
        path.append((x, y))
    return path


# setup lists
path = []
visited = set()
queue = deque()
solution = {}

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

Road = Road()
locationslst=[[500,50],[150,325],[550,500],[1000,150]]




possible_traffic=[]

for i in Road.coordinates:
    x,y=i
    if i not in locationslst:
        #since we are checking at interval of 25 units
        if x%25==0 and y%25==0:
            possible_traffic.append([x,y])

#randomly chooses vertices for traffic
global traffic
traffic = []
for i in range(traffic_intensity*2):
    a = random.choice(possible_traffic)
    traffic.append(a)
    possible_traffic.remove(a)
print(traffic)

for i in traffic:
    while i in Road.coordinates:
        Road.coordinates.remove(i)
    print(i)


######
start_x, start_y = start
end_x, end_y = end
search(start_x, start_y)

path = backRoute(end_x, end_y)
path = path[::-1]
print(path)



def next_turn(path, x=6.5, y=6):
    show_path = canvas.create_rectangle(10, 10, 20, 20, fill='red', outline='', width=0)

    try:
        x2 = path[0][0]
        y2 = path[0][1]
    except IndexError:
        return
    if (x2, y2) in traffic:
        window.after(5000)

    u = path.pop(0)
    x = x2 - x
    y = y2 - y
    canvas.move(show_path, x, y)
    window.after(500, next_turn, path)


next_turn(path)

#adding images
filename = "C:\\Users\\Dell 7240\\Downloads\\download.png"
img = Image.open(filename)
img = img.resize((20, 20), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
for i in traffic:
    canvas.create_image(i[0], i[1], image=img)


school = Image.open("C:\\Users\\Dell 7240\\Downloads\\school.png")
school = school.resize((70, 70), Image.ANTIALIAS)
school = ImageTk.PhotoImage(school)
canvas.create_image(locations['School'][0], locations['School'][1], image=school)

hospital = Image.open("C:\\Users\\Dell 7240\\Downloads\\hospital.png")
hospital = hospital.resize((70, 70), Image.ANTIALIAS)
hospital = ImageTk.PhotoImage(hospital)
canvas.create_image(locations['Hospital'][0], locations['Hospital'][1], image=hospital)

home = Image.open("C:\\Users\\Dell 7240\\Downloads\\home.jpg")
home = home.resize((70, 70), Image.ANTIALIAS)
home = ImageTk.PhotoImage(home)
canvas.create_image(locations['Home'][0], locations['Home'][1], image=home)

park = Image.open("C:\\Users\\Dell 7240\\Downloads\\park.png")
park = park.resize((70, 70), Image.ANTIALIAS)
park = ImageTk.PhotoImage(park)
canvas.create_image(locations['Park'][0], locations['Park'][1], image=park)

tt = ('No traffic','Light','Medium','Heavy')


# printing text
window.after(speed, next_turn, path)
distance = len(path) // 20
print(len(path))
time = distance / speed_mode
time = time + ((2 / 60) * traffic_intensity)
time = int(time * 60)

textt = str('MOT: ') + str(mode) + str('\nTraffic intensity: ') + str(tt[traffic_intensity]) + str('\nTime to reach ') + str(y) + ': ' + str(int(time)) + str(' mins') + str("\nDistance: ") + str(distance) + str(' km')

a = Label(window, text=textt)
a.configure(foreground="white", background='black', font=('Courier', 14))
a.pack()
a.place(relx=0.96, rely=0.25, anchor='ne')
window.mainloop()