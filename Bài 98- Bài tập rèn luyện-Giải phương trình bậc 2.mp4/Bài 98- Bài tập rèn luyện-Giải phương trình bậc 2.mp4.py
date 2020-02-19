from tkinter import *
from firstDegreeEquation import firstDEqual
from SecondDegreeEquation import SecondDEqual


def continueAct():
    fac_A.set('')
    fac_B.set('')
    fac_C.set('')
    Result.set('')
def calculateAct():
    a = float(fac_A.get())
    b = float(fac_B.get())
    c = float(fac_C.get())
    if a == 0:
        Result.set(firstDEqual(b,c))
    else:
        Result.set(SecondDEqual(a,b,c))


root = Tk()
fac_A = StringVar()
fac_B = StringVar()
fac_C = StringVar()
Result = StringVar()



root.title('second degree equation')
root.minsize(width=550,height=300)
root.resizable(width=True,height=True)
Label(root,text = "Second Degree Equation",font = 'helvetica,20',fg = 'green',justify = CENTER).grid(row = 0, columnspan = 2)

Label(root,text = "factor A").grid(row = 1, column = 0)
Entry(root,width= 60, textvariable = fac_A).grid(row = 1, column = 1)

Label(root,text = "factor B").grid(row = 2, column = 0)
Entry(root,width= 60, textvariable = fac_B ).grid(row = 2, column = 1)

Label(root,text = "factor C").grid(row = 3, column = 0)
Entry(root,width= 60, textvariable = fac_C).grid(row = 3, column = 1)

ButtonFrames = Frame()
Button(ButtonFrames,text = 'Calculate',width = 10, command = calculateAct).pack(side=LEFT)
Button(ButtonFrames,text = 'Continue',width = 10, command = continueAct).pack(side=LEFT)
Button(ButtonFrames,text = 'Exit',width = 10, command = root.quit).pack(side=LEFT)
ButtonFrames.grid(row = 4, columnspan = 3)

Label(root,text = "RESULT").grid(row = 5, column = 0)
Entry(root,width= 60, textvariable = Result).grid(row = 5, column = 1)

root.mainloop()