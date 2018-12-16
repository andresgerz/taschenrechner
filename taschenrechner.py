# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 23:44:09 2018

@author: mellisos
"""
from tkinter import * 

root=Tk()

myFrame=Frame(root)
myFrame.pack()

operation=""
result=0

##################screen#############################
screenNumber=StringVar()   

screen=Entry(myFrame, textvariable=screenNumber)
screen.grid(row=0 ,column=0 ,pady=5 ,padx=5 ,columnspan=4)
screen.config(background="green",fg="blue",justify="right")


def numberPress(n):
    
    global operation 
    
    if operation!="" :
        screenNumber.set(n)
    
        operation=""
        
    else:
        screenNumber.set(screenNumber.get() + n)    


def addition(n):
    
    global operation
    global result
    
    result+=(int(n))
    
    operation = "addition"  
    
    screenNumber.set(result)


def multiply(n): #NOT FUNCTION!
    
    global operation
    global result
    
    result=(int(n))*result
    
    
    operation="multiply"

    screenNumber.set(result)
    

def the_result():
    
    global result
    
    screenNumber.set(result+int(screenNumber.get()))
    screenNumber.set(result*int(screenNumber.get()))

    
# # subtract
# 
# division
# 
# multiply       


button7=Button(myFrame,text="7", width=4, command = lambda:numberPress("7"))
button7.grid(row=2, column=0)

button8=Button(myFrame,text="8", width=4, command = lambda:numberPress("8"))
button8.grid(row=2, column=1)

button9=Button(myFrame,text="9", width=4, command = lambda:numberPress("9"))
button9.grid(row=2, column=2)

button4=Button(myFrame,text="4", width=4, command = lambda:numberPress("4"))
button4.grid(row=3, column=0)

button5=Button(myFrame,text="5", width=4, command = lambda:numberPress("5"))
button5.grid(row=3, column=1)

button6=Button(myFrame,text="6", width=4, command = lambda:numberPress("6"))
button6.grid(row=3, column=2)

button1=Button(myFrame,text="1", width=4, command = lambda:numberPress("1"))
button1.grid(row=4, column=0)

button2=Button(myFrame,text="2", width=4, command = lambda:numberPress("2"))
button2.grid(row=4, column=1)

button3=Button(myFrame,text="3", width=4, command = lambda:numberPress("3"))
button3.grid(row=4, column=2)

button0=Button(myFrame,text="0", width=4, command = lambda:numberPress("0"))
button0.grid(row=5, column=0)

buttonDiv=Button(myFrame ,text="/" ,width=4)
buttonDiv.grid(row=2, column=3)

buttonMult=Button(myFrame ,text="*" ,width=4, command=lambda:multiply(screenNumber.get()))
buttonMult.grid(row=3, column=3)

buttonAdd=Button(myFrame ,text="+" ,width=4, command=lambda:addition(screenNumber.get()))
buttonAdd.grid(row=4, column=3)

buttonSubtr=Button(myFrame ,text="-" ,width=4)
buttonSubtr.grid(row=5, column=3)

buttonSubtr=Button(myFrame ,text="=" ,width=4, command=lambda:the_result())
buttonSubtr.grid(row=5, column=1)

buttonSubtr=Button(myFrame ,text="," ,width=4, command = lambda:numberPress(","))
buttonSubtr.grid(row=5, column=2)

root.mainloop()