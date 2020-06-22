from tkinter import *
top = Tk()
def a():
    a = en.get()
    a = a.split('*')
    lb1["text"] = "받은 값: " + str(int(a[0]) * int(a[1]))
    
en = Entry(top)
bt1 = Button(top,text = "곱",command = a)
lb1 = Label(top,text="")
en.grid(row =0 ,column = 0)
bt1.grid(row =1 ,column = 0)
lb1.grid(row =2 ,column = 0)


top.mainloop()
