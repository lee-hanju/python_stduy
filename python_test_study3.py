from tkinter import *
top = Tk()
top.title("제목")

def output():
    a = en1.get()
    # 값을 들고오는역할
    #textBox에서 받은값
    
    lb1["text"] = "받은 값 : "+ str(a)
#첫번째칸은 폼 선택
#두번째칸은 text 
#width, height

#버튼만 command

en1 = Entry(top)
btn1 = Button(top, text ="입력", command=output)
lb1 = Label(top, text="")
en1.grid(row=0, column=0)
btn1.grid(row=1, column=0)
lb1.grid(row=2, column=0)
#grid pack 같이 못써
#grid(row, column)
#pack(side=LEFT)
#RIGHT TOP BOTTOM

top.mainloop()
#Entry - textBox
#Button 
#Label
#Radiobutton - 라디오박스
#Checkbutton - 체크박스
