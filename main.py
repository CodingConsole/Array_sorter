from tkinter import *
from datetime import *
import generator as gen

def generate():#activates generator and displays arrays
    global elements, elements2
    
    g.generate()
    
    for i in range(100):
        elements[i].config(text = g.field[i])

    g.sort_1()
    
    for i in range(100):
        elements2[i].config(text = g.sorted[i])

def quit():
    root.destroy()

#-------//INIT ROOT + ELEMENTS//-------#

root = Tk()#configurate root
root.title("Array-sorter")
root.geometry("1500x900")
root.resizable(0, 0)

g = gen.generator()#create generator
    
#-------//GRAPHICS + BUTTONS//-------#
canvas = Canvas(root, width = 1505, height = 905)
canvas.place(x = -5,y = -5)
canvas.config(background = '#d4d4d4')
canvas.create_line(0, 85, 1505, 85, width = 5)#horizontal line
canvas.create_line(748, 85, 748, 905, width = 5)#vertical line

#init labels which output lists
elements = list(range(100))#unsorted list
counter = 0; cx = 30; cy = 170
for i in range(100):
    elements[i] = Label(root, text = "0", font=("Arial", 15), background = '#d4d4d4')
    elements[i].place(x = cx, y = cy)
    counter += 1; cx += 70
    if (counter == 10):
        counter = 0; cy += 70; cx = 30;
    
elements2 = list(range(100))#sorted list
counter = 0; cx = 783; cy = 170
for i in range(100):
    elements2[i] = Label(root, text = "0", font=("Arial", 15), background = '#d4d4d4')
    elements2[i].place(x = cx, y = cy)
    counter += 1; cx += 70
    if (counter == 10):
        counter = 0; cy += 70; cx = 783;

b_generate = Button(root, text = "Generate", font=("Arial", 15), command = lambda : generate())
b_generate.pack()
b_generate.place(x = 20, y = 20)

b_quit = Button(root, text = "Quit", font=("Arial", 15), command = lambda : quit())
b_quit.pack()
b_quit.place(x = 1400, y = 20)

l_generated = Label(root, text="Generated", font=("Arial", 15), background = '#d4d4d4')
l_generated.place(x = 30, y = 100)

l_sorted = Label(root, text="Sorted", font=("Arial", 15), background = '#d4d4d4')
l_sorted.place(x = 783, y = 100)

root.mainloop()
