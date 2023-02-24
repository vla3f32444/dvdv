from tkinter import *

root = Tk()
root.geometry('500x500')

b=''
def click():
    b=a.get()
    Label(root,text=('здравствуйте,',b)).pack()

Button(root,text='entry',command=click).pack()

Label(root,text=('здравствуйте,',b)).pack()

a=Entry(root)
a.pack()

root.mainloop()