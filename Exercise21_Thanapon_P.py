from tkinter import *
import math

def leftClickButton(event):
    Heigh = float(textBoxWeight.get())
    Weight = math.pow(float(textBoxHeight.get())/100,2)
    bmi = Heigh/Weight
    labelBMI.configure(text = "BMI = "+str(bmi))
    if bmi<18.5 :
        bmiResult = "ผอมเกินไป"
    elif 18.6 <= bmi <= 22.9:
        bmiResult = "น้ำหนักปกติ เหมาะสม"
    elif 23 <= bmi <= 24.9:
        bmiResult = "น้ำหนักเกิน"
    elif 25 <= bmi <= 29.9:
        bmiResult = "อ้วน"
    elif bmi > 30:
        bmiResult = "อ้วนมาก"
    labelResult.configure(text=bmiResult)

MainWindow = Tk()
labelHeight = Label(MainWindow, text="ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeigth = Label(MainWindow, text="น้ำหนัก (Kg.)")
labelWeigth.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text = "คำนวน")
calculateButton.bind("<Button-1>",leftClickButton)
calculateButton.grid(row=2,column=0)
labelResult = Label(MainWindow,text="ผลลัพท์")
labelResult.grid(row=2,column=1)
labelBMI = Label(MainWindow,text="BMI = ",anchor = CENTER)
labelBMI.grid(row=3,column=1)

MainWindow.mainloop()