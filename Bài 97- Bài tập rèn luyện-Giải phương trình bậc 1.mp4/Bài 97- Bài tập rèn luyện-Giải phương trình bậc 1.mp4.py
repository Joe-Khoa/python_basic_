from tkinter import *
def CalAction():
    a = float(stringNoA.get())
    b = float(stringNoB.get())
    if a == 0 and b == 0:
        stringKQ.set('imnumerable roots')
    elif a == 0 and b != 0:
        stringKQ.set('not exist root')
    else:
        stringKQ.set(str(-b/a))
def continueAction():
    stringNoA.set('')
    stringNoB.set('')
    stringKQ.set('')

root = Tk()

stringNoA = StringVar()
stringNoB = StringVar()
stringKQ = StringVar()


root.title('first degree equation: ')
root.minsize(width=600,height=400)
root.resizable(width=True,height=True)
Label(root,text = 'first degree equation', fg = 'red', font = 'Helvetica,18').grid(row = 0 , columnspan = 2)

Label(root,text= 'Index a : ').grid(row = 1,column = 0)
Entry(root,width = 50,textvariable = stringNoA ).grid(row = 1, column = 1)

Label(root,text = 'Index b : ').grid(row = 2, column = 0)
Entry(root,width = 50, textvariable = stringNoB).grid(row = 2, column = 1)

FrameButtons = Frame()
Button(FrameButtons,text = 'Calculate',command = CalAction).pack(side = LEFT)
Button(FrameButtons,text = 'Continue',command = continueAction).pack(side = LEFT)
Button(FrameButtons,text = 'Exit', command=root.quit).pack(side = LEFT)
FrameButtons.grid(row =3, columnspan = 2)

Label(root,text = 'Result').grid(row = 4, column =0)
Entry(root,width = 40, textvariable = stringKQ).grid(row = 4, column = 1)

root.mainloop()
