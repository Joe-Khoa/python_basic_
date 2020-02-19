from tkinter import *
root = Tk()
root.title('http:tkinter.com/vndomain')
root.resizable(height=True,width=True)
root.minsize(width=700,height=400)

Label(root,text = 'hello tkinter',fg = 'green').pack()
Button(root,text = 'click here',command = root.quit).pack()
e = StringVar()
e.set("nonStop-community")
Entry(root,textvariable = e,width = 30).pack()
root.mainloop()