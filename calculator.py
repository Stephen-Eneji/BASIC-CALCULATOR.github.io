from tkinter import *
import time
from tkinter import messagebox

df = "Arial 20"
bf = "Tahoma 20"
def click(event):
    try:
        global scvalue
        text = event.widget.cget("text")
        text = str(text)
        if text=="=":
            if scvalue.get().isdigit():
                value = int(scvalue.get())
            else:
                value = eval(scvalue.get())
            scvalue.set(value)
            screen.update()
        elif text=="C":
            scvalue.set("")
            screen.update()

        else:
            scvalue.set(scvalue.get() + text)
            screen.update()
    except Exception:
        messagebox.showinfo("Error","You Are Entered something wrong")
        time.sleep(0.5)
        scvalue.set("")




class GUI(Tk):
    def __init__(self, *args):
        super().__init__()
        self.geometry("300x380+400+200")
        self.title("CALCULATOR - Prototype ")

    def butt(self, win, name, x, y, pady, bg, padx,font):
        b = Button(win, text=name, font=font, bg=bg,fg="white")
        b.place(x=x,y=y, height=pady, width=padx)
        b.bind("<Button-1>",click)




if __name__ == '__main__':
    window = GUI()


    scvalue = StringVar()
    scvalue.set("")
    screen = Entry(window, textvariable=scvalue, bg="#f4cccc", fg="#cc0000" ,font=df, relief=SUNKEN,bd=9)
    screen.place(x=0,y=0,height=50, width=300)
#this is a list that contains the position of all the buttons

    button_list= ["C","7","8","9","/","4","5","6","*","1","2","3",".","0","-","+","="]
    x_pos = ["5","5","80","155","230","5","80","155","230","5","80","155","230","5","100","195","5"]
    y_pos = ["50","105","105","105","105","160","160","160","160","215","215","215","215","270","270","270","325"]
    padx = ["290","75","75","75","65","75","75","75","65","75","75","75","65","96","96","99","290"]
    pady = ["50","50","50","50","50","50","50","50","50","50","50","50","50","50","50","50","50"]

#these are the list index variable that can be incrimented with the loop ittereter

    bt = 0
    xpo = 0
    ypo = 0
    pax = 0
    pay = 0

    for i in range(17):
        window.butt(window,button_list[bt],x=x_pos[xpo],y=y_pos[ypo],padx=padx[pax],pady=pady[pay],font=bf, bg="#1155cc")
        bt+=1
        xpo+=1
        ypo+=1
        pax+=1
        pay+=1



    window.config(bg="#cfe2f3")
    window.mainloop()
