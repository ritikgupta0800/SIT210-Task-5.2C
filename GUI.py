from tkinter import *
import tkinter.font
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40,GPIO.OUT)
GPIO.output(40,GPIO.LOW)
GPIO.setup(38,GPIO.OUT)
GPIO.output(38,GPIO.LOW)
GPIO.setup(36,GPIO.OUT)
GPIO.output(36,GPIO.LOW)
GPIO.setwarnings(False)
win = Tk()

myFont = tkinter.font.Font(family='Helvetica', size = 30, weight = 'bold')

def redledON():
    print("red LED button pressed")
    if GPIO.input(40):
        GPIO.output(40,GPIO.LOW)
        ledButton["text"] = "RED LED ON"
    else:
        GPIO.output(40,GPIO.HIGH)
        ledButton["text"] = "RED LED OFF"

def greenledON():
    print("green LED button pressed")
    if GPIO.input(38):
        GPIO.output(38,GPIO.LOW)
        ledButton["text"] = "GREEN LED ON"
    else:
        GPIO.output(38,GPIO.HIGH)
        ledButton["text"] = "GREEN LED OFF"
        
def blueledON():
    print("blue LED button pressed")
    if GPIO.input(36):
        GPIO.output(36,GPIO.LOW)
        ledButton["text"] = "BLUE LED ON"
    else:
        GPIO.output(36,GPIO.HIGH)
        ledButton["text"] = "BLUE LED OFF"

def exitProgram():
    print("Exit button pressed")
    GPIO.cleanup()
    win.quit()
    
win.title("GUI")


exitButton = Button(win, text = "EXIT", font = myFont , command = exitProgram, height = 2, width = 6)
exitButton.pack()

ledButton = Button(win, text = "RED led ON", font = myFont , command = redledON, height = 2, width = 15)
ledButton.pack()

ledButton = Button(win, text = "GREEN led ON", font = myFont , command = greenledON, height = 2, width = 15)
ledButton.pack()

ledButton = Button(win, text = "BLUE led ON", font = myFont , command = blueledON, height = 2, width = 15)
ledButton.pack()

mainloop()
