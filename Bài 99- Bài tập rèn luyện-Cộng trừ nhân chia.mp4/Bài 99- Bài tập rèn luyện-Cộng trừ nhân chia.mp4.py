from tkinter import *
from calculatingFnc import calculatingFnc
def ClearAll():
    No_A.set('')
    No_B.set('')
    RESULT.set('')


def AddAction():
    a = float(No_A.get())
    b = float(No_B.get())
    RESULT.set(str(calculatingFnc(a,b,'+')))
def SubAction():
    a = float(No_A.get())
    b = float(No_B.get())
    RESULT.set(str(calculatingFnc(a,b,'-')))
def MultAction():
    a = float(No_A.get())
    b = float(No_B.get())
    RESULT.set(str(calculatingFnc(a,b,'*')))
def DevAction():
    a = float(No_A.get())
    b = float(No_B.get())
    RESULT.set(str(calculatingFnc(a,b,'/')))

# def handle2No(f,x,y,op):
#     return f(x,y,op)
# kq3 = handle2(lambda x,y:x+y,2,3)

x = Tk()

No_A = StringVar()
No_B = StringVar()
RESULT = StringVar()



x.title('Simple Calculator')
x.minsize(width=500,height=300)
x.resizable(width=True,height = True)
Label(x,text = 'Simple Calculator',font = 'Helvetica,30', justify= CENTER, fg = 'RED').grid( row= 0, columnspan = 3)

ButtonsFrame = Frame(x)
Button(ButtonsFrame,text = 'Add', command = AddAction).pack(side=TOP, fill = X)
Button(ButtonsFrame,text = 'Subtract', command = SubAction).pack(side=TOP, fill = X)
Button(ButtonsFrame,text = 'Multiple', command = MultAction).pack(side=TOP, fill = X)
Button(ButtonsFrame,text = 'Devide', command = DevAction).pack(side=TOP, fill = X)
ButtonsFrame.grid(row = 1,column = 0, rowspan = 4)

Label(x, text = 'text No A').grid(row = 1, column = 1)
Entry(x, width = 20, textvariable = No_A).grid(row = 1, column = 2)
Label(x, text = 'text No B').grid(row = 2, column = 1)
Entry(x, width = 20, textvariable = No_B).grid(row = 2, column = 2)
Label(x, text = 'RESULT').grid(row = 3, column = 1)
Entry(x, width = 20, textvariable = RESULT).grid(row = 3, column = 2)

Button(x, text = 'Exit', command = x.quit).grid( row = 4, column  = 2)
Button(x, text = 'Clear All', command = ClearAll).grid( row = 4, column  = 3)

x.mainloop()