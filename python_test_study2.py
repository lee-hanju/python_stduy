from tkinter import*
top = Tk()

def result():
    string = ""
    if select1.get()==1:
        string += "앙"
    if select2.get()==1:
        string += "기"
    if select3.get()==1:
        string += "모"
    if select4.get()==1:
        string += "띠"
    lb1["text"] = string

select1 = IntVar()
select2 = IntVar()
select3 = IntVar()
select4 = IntVar()
ck1 = Checkbutton(top,text = "앙",variable=select1)
ck2 = Checkbutton(top,text = "기",variable=select2)
ck3 = Checkbutton(top,text = "모",variable=select3)
ck4 = Checkbutton(top,text = "띠",variable=select4)
bt = Button(top,text="췕",command=result )
lb1 = Label(top,text = "")
ck1.grid(row = 0,column=0)
ck2.grid(row=1,column=0)
ck3.grid(row=2,column=0)
ck4.grid(row=3,column=0)
bt.grid(row=4,column=0)
lb1.grid(row=5,column=0)


top.mainloop()
