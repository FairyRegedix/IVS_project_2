# -*- coding: utf-8 -*-
from tkinter import *
import math_lib as math

err_msg = "Syntax ERROR"

"""Checks if string is convertible to integer

Returns:
    bool -- Can/Can't be converted
"""
def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

"""Checks if string is convertible to float

Returns:
    bool -- Can/Can't be converted
"""
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

"""Replaces part of the equation with the result
"""
def replace(result, temp, i):
    result.remove(result[i-1])
    result.remove(result[i-1])
    result.remove(result[i-1])
    result.insert(i-1, str(temp))

"""Sets error message
"""
def set_err_msg(result, err_msg):
    result.clear()
    result.append(err_msg)

"""Calculating low priority operations

Returns:
    int -- Counter
"""
def low_priority_op(result, temp, i):
    if result[i] == '+':
        if (i-1) < 0 and is_float(result[i+1]):
            result.remove(result[i]) 
        elif (i+1) > len(result) - 1:
            set_err_msg(result, err_msg)
            return 0 
            #TODO: Instead of error disable =
        elif is_float(result[i-1]) and is_float(result[i+1]):
            temp = math.add(float(result[i-1]), float(result[i+1]))
            replace(result, temp, i)
            i -= 1
        elif not is_float(result[i-1]) or not is_float(result[i+1]):
            set_err_msg(result, err_msg)
            return 0

    if result[i] == '-':
        if (i-1) < 0 and is_float(result[i+1]):
            temp = - float(result[i+1])
            result.remove(result[i])
            result.remove(result[i])
            result.insert(i, str(temp))
        elif (i+1) > len(result) - 1:
            set_err_msg(result, err_msg)
            return 0 
            #TODO: Instead of error disable =
        elif is_float(result[i-1]) and is_float(result[i+1]):
            temp = math.sub(float(result[i-1]), float(result[i+1]))
            replace(result, temp, i)
            i -= 1
        elif not is_float(result[i-1]) or not is_float(result[i+1]):
            set_err_msg(result, err_msg)
            return 0

    return (i + 1)

"""Calculating middle priority operations

Returns:
    int -- Counter
"""
def mid_priority_op(result, temp, i):
    if result[i] == '*':
        if (i-1) < 0 :
            set_err_msg(result, err_msg)
            return 0 
        elif (i+1) > len(result) - 1:
            set_err_msg(result, err_msg)
            return 0 
            #TODO: Instead of error disable =
        elif is_float(result[i-1]) and is_float(result[i+1]):
            temp = math.mul(float(result[i-1]), float(result[i+1]))
            replace(result, temp, i)
            i -= 1
        elif not is_float(result[i-1]) or not is_float(result[i+1]):
            set_err_msg(result, err_msg)
            return 0
            
    if result[i] == '/':
        if (i-1) < 0:
            set_err_msg(result, err_msg)
            return 0 
        elif (i+1) > len(result) - 1:
            set_err_msg(result, err_msg)
            return 0 
            #TODO: Instead of error disable =
        elif is_float(result[i-1]) and is_float(result[i+1]):
            temp = math.div(float(result[i-1]), float(result[i+1]))
            replace(result, temp, i)
            i -= 1
        elif not is_float(result[i-1]) or not is_float(result[i+1]):
            set_err_msg(result, err_msg)
            return 0 
    return (i + 1)

"""Calculating high priority operations

Returns:
    int -- Counter
"""
def high_priority_op(result, temp, i):
    if result[i] == '^':
        if (i-1) < 0 :
            set_err_msg(result, err_msg)
            return 0 
        elif (i+1) > len(result) - 1:
            set_err_msg(result, err_msg)
            return 0 
            #TODO: Instead of error disable =
        elif is_float(result[i-1]) and is_float(result[i+1]):
            temp = math.exp(float(result[i-1]), float(result[i+1]))
            replace(result, temp, i)
            i -= 1
        elif not is_float(result[i-1]) or not is_float(result[i+1]):
            set_err_msg(result, err_msg)
            return 0
            
    if result[i] == '√':
        if (i+1) > len(result) - 1:
            set_err_msg(result, err_msg)
            return 0 
            #TODO: Instead of error disable =
        elif is_float(result[i+1]):
            temp = math.ext(float(result[i+1]), 2)
            result.remove(result[i])
            result.remove(result[i])
            result.insert(i, str(temp))
            i -= 1
        elif not is_float(result[i+1]):
            set_err_msg(result, err_msg)
            return 0 
    return (i + 1)

def highest_priority_op(result, temp, i):
    if result[i] == '!':
        if (i+1) > len(result) - 1:
            set_err_msg(result, err_msg)
            return 0 
            #TODO: Instead of error disable =
        elif is_integer(result[i+1]) and int(result[i+1]) >= 0:
            temp = math.fact(int(result[i+1]))
            result.remove(result[i])
            result.remove(result[i])
            result.insert(i, str(temp))
            i -= 1
        elif not is_integer(result[i+1]) or int(result[i+1]) < 0:
            set_err_msg(result, err_msg)
            return 0 
    return (i + 1)

"""Performs the calculation of the equation

Returns:
    string -- Result of equation
"""
def calculate(result):
    temp = 0
    i = 0
    result = result.split()
    # Going through each member of the list to check for signs
    if len(result) <= 1:
        result.clear()
        return result
    while(len(result) > 1):
        while(result.count('!') != 0):
            i = highest_priority_op(result, temp, i)
        else:
            i = 0
        while(result.count('^') != 0 or result.count('√') != 0):
            i = high_priority_op(result, temp, i)
        else:
            i = 0
        while(result.count('*') != 0 or result.count('/') != 0):
            i = mid_priority_op(result, temp, i)
        else:
            i = 0
        while(result.count('+') != 0 or result.count('-') != 0):
            i = low_priority_op(result, temp, i)
        else:
            i = 0

    return result[0]   

"""Calculator class, holds the entire gui code
"""
class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("CalculaThor")

        # text screen
        self.screen = Text(master, state='disabled', width=32, height=5,border = 1,background="light grey", foreground="blue")

        # position screen in window
        self.screen.grid(row=0,column=0,columnspan=4,padx=5,pady=5)
        self.screen.configure(state='normal')

        # create buttons using method createButton
        button1 = Button(root,text='1',width=8, height=2, command=lambda: self.buttonClick('1'))
        button2 = Button(root,text='2',width=8, height=2, command=lambda: self.buttonClick('2'))
        button3 = Button(root,text='3',width=8, height=2, command=lambda: self.buttonClick('3'))
        button4 = Button(root,text='4',width=8, height=2, command=lambda: self.buttonClick('4'))
        button5 = Button(root,text='5',width=8, height=2, command=lambda: self.buttonClick('5'))
        button6 = Button(root,text='6',width=8, height=2, command=lambda: self.buttonClick('6'))
        button7 = Button(root,text='7',width=8, height=2, command=lambda: self.buttonClick('7'))
        button8 = Button(root,text='8',width=8, height=2, command=lambda: self.buttonClick('8'))
        button9 = Button(root,text='9',width=8, height=2, command=lambda: self.buttonClick('9'))
        button10 = Button(root,text='0',width=18, height=2, command=lambda: self.buttonClick('0'))  
        button11 = Button(root,text='.',width=8, height=2, command=lambda: self.buttonClick('.'))
        button12 = Button(root,text='+',width=8, height=2, command=lambda: self.buttonClick(' + '))
        button13 = Button(root,text='-',width=8, height=2, command=lambda: self.buttonClick(' - '))
        button14 = Button(root,text='*',width=8, height=2,background='orange', command=lambda: self.buttonClick(' * '))
        button15 = Button(root,text='/',width=8, height=2,background='orange', command=lambda: self.buttonClick(' / '))
        button16 = Button(root,text='=',width=8, height=5,background='orange', command=lambda: self.buttonClick('eq'))
        button17 = Button(root,text='|x|',width=8, height=2, command=lambda: self.buttonClick('abs'))  
        button18 = Button(root,text='^',width=8, height=2, command=lambda: self.buttonClick(' ^ '))
        button19 = Button(root,text='√',width=8, height=2,background='orange', command=lambda: self.buttonClick(' √ '))
        button20 = Button(root,text='AC',width=8, height=2, command=lambda: self.clear())
        button21 = Button(root,text='DEL',width=8, height=2,background='orange', command=lambda: self.buttonClick('del'))
        button22 = Button(root,text='!',width=8, height=2, command=lambda: self.buttonClick(' ! '))

        # buttons stored in list
        buttons = [button20,button17,button18,button19,button22,button12,button13,button21,button7,button8,button9,button15,
        button4,button5,button6,button14,button1,button2,button3,button10,button11,button16]

        # intialize counter
        count = 0
        # arrange buttons with grid manager
        for row in range(1,6): #rows
            for column in range(4): #column
                buttons[count].grid(row=row,column=column)
                count += 1
        #arrange last line
        # arrange "0"
        buttons[19].grid(row=6,column=0,columnspan=2)
        #arrange ","
        buttons[20].grid(row=6,column=2)
        #arrange "="
        buttons[21].grid(row=5,column=3,rowspan=2)
    
    """Method to clear the screen
    """
    def clear(self):
        self.screen.delete("1.0", END)

    """Function decides whether to delete one or three characters depending on the last character on screen
    """
    def screen_del(self):
        scr_text = self.screen.get("1.0", END)
        scr_text = scr_text.split()
        if(is_float(scr_text[len(scr_text)-1]) or is_integer(scr_text[len(scr_text)-1])):
            self.screen.delete("end-2c", END)
        else:
            self.screen.delete("end-4c", END)

    """This function creates a button, and takes one compulsory argument, the value that should be on the button
    """
    def createButton(self,val,write=True,width=5):
        return Button(self.master, text=val,command = lambda: self.click(val,write), width=8, height = 2)

    """Checks the button type, if it's a number or operand it gets typed out into the text box, otherwise function
       calls occur
    """
    def buttonClick(self,butt_type):
        if(butt_type == 'del'):
            self.screen_del()
        elif(butt_type == 'eq'):
            equation = self.screen.get("1.0", END)
            self.clear()
            result = calculate(equation)
            self.screen.insert(END, result)
        elif(butt_type == 'abs'):
            result = str(math.abs(float(self.screen.get("1.0", END))))
            self.clear()
            self.screen.insert(END, result)
        else:
            self.screen.insert(END, butt_type)
        
        
"""End of Calculator class
"""

root = Tk()
root.iconphoto(False, PhotoImage(file='src/mjolnir.ico'))
root.geometry("269x342")
my_gui = Calculator(root)


root.mainloop()
