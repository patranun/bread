from tkinter import *
import math

def leftclick(event):
    print(float(textBoxweight.get())/math.pow(float(textBox.get())/100,2))
    labelResult.configure(text= float(textBoxweight.get())/math.pow(float(textBox.get())/100,2))

def BMI (event):
    bmi1 = float(textBoxweight.get()) / math.pow(float(textBox.get()) / 100, 2)
    if bmi1 < 18.5:
        print('ผอมมาก')
        labelBMI.configure(text='ผอมมาก')
    elif bmi1 < 23.5 and bmi1 > 18.5:
        print('ผอม')
        labelBMI.configure(text='ผอม')
    elif bmi1 > 23.5 and bmi1 < 26.5:
        print('ปกติ')
        labelBMI.configure(text='ปกติ')
    elif bmi1 > 26.5 and bmi1 < 29.9:
        print('อ้วน')
        labelBMI.configure(text='อ้วน')
    elif bmi1 > 29.9:
        print('อ้วนมาก')
        labelBMI.configure(text='อ้วนมาก')
    print(bmi1)



mainWindow = Tk()
labelheight = Label(mainWindow,text = 'ส่วนสูง (cm.)')
labelheight.grid(row = 0,column =0)
textBox = Entry(mainWindow)
textBox.grid(row = 0, column = 1)
labelweight = Label(mainWindow,text = 'น้ำหนัก (Kg.)')
labelweight.grid(row = 1,column = 0)
textBoxweight = Entry(mainWindow)
textBoxweight.grid(row =1,column = 1)
calculatebutton = Button(mainWindow,text = 'คำนวณ')
calculatebutton.bind('<Button-1>',leftclick)
calculatebutton.grid(row=2,column = 0)
labelResult = Label(mainWindow,text = 'ผลลัพธ์')
labelResult.grid(row = 2,column =1)
calculatebutton2 = Button(mainWindow,text = 'BMI')
calculatebutton2.bind('<Button-1>',BMI)
calculatebutton2.grid(row=3,column = 0)
labelBMI = Label(mainWindow,text = 'BMI')
labelBMI.grid(row = 3,column = 1)
mainWindow.mainloop()

