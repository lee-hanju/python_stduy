from tkinter import *
top = Tk()
def result():
    if select1.get() == 1:
        print("체크1")
    if select2.get() == 1:
        print("체크2")
    if select3.get() == 1:
        print("체크3")
select1 =IntVar()
select2 =IntVar()
select3 =IntVar()
chk1 = Checkbutton(top, text="체크1",variable=select1)
chk2 = Checkbutton(top, text="체크2",variable=select2)
chk3 = Checkbutton(top, text="체크3",variable=select3)
btn = Button(top, text= "check",command=result)
chk1.pack()
chk2.pack()
chk3.pack()
btn.pack()

top.mainloop()
