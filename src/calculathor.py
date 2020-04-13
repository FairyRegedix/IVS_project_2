from tkinter import *

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Kaukuacka")

        # text screen
        self.screen = Text(master, state='disabled', width=32, height=5,border = 1,background="light grey", foreground="blue")

        # position screen in window
        self.screen.grid(row=0,column=0,columnspan=4,padx=5,pady=5)
        self.screen.configure(state='normal')

        # initialize screen value as empty
        self.equation = ''

        # create buttons using method createButton
        button1 = Button(root,text='1',width=8, height=2)
        button2 = Button(root,text='2',width=8, height=2)
        button3 = Button(root,text='3',width=8, height=2)
        button4 = Button(root,text='4',width=8, height=2)
        button5 = Button(root,text='5',width=8, height=2)
        button6 = Button(root,text='6',width=8, height=2)
        button7 = Button(root,text='7',width=8, height=2)
        button8 = Button(root,text='8',width=8, height=2)
        button9 = Button(root,text='9',width=8, height=2)
        button10 = Button(root,text='0',width=18, height=2)  
        button11 = Button(root,text=',',width=8, height=2)
        button12 = Button(root,text='+',width=8, height=2)
        button13 = Button(root,text='-',width=8, height=2)
        button14 = Button(root,text='*',width=8, height=2,background='orange')
        button15 = Button(root,text='/',width=8, height=2,background='orange')
        button16 = Button(root,text='=',width=8, height=5,background='orange')
        button17 = Button(root,text='|x|',width=8, height=2)  
        button18 = Button(root,text='**',width=8, height=2)
        button19 = Button(root,text='//',width=8, height=2,background='orange')
        button20 = Button(root,text='AC',width=8, height=2)
        button21 = Button(root,text='DEL',width=8, height=2,background='orange')
        button22 = Button(root,text='!',width=8, height=2)

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
    
    def createButton(self,val,write=True,width=5):
        # this function creates a button, and takes one compulsory argument, the value that should be on the button

        return Button(self.master, text=val,command = lambda: self.click(val,write), width=8, height = 2)

root = Tk()
root.geometry("269x342")
my_gui = Calculator(root)


root.mainloop()